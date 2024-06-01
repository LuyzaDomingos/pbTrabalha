from flask import Flask, render_template, jsonify

import data_manager as dm
import plotter as pltr

app = Flask(__name__)


@app.route('/')
def index():
    return general()


@app.route('/all/<selected_date>')
def general(selected_date: str = "2024-02-01"):
    stats = dm.adm_layoffs_series[dm.adm_layoffs_series["competênciamov"] ==
                                  selected_date].astype({"competênciamov": str}).to_dict(orient="records")
    if len(stats) > 0:
        return render_template('index.html',
                               date=selected_date,
                               dates=[str(date).split("T")[0] for date in reversed(dm.data["competênciamov"].unique())
                                      if str(date).split("T")[0] != selected_date],
                               # cities=["Paraíba"] + [city for city in dm.cities],
                               stats=stats[0],
                               plot1=pltr.create_adm_layoff_plot(dm.adm_layoffs_series.set_index("competênciamov")),
                               plot2=pltr.create_net_plot(dm.net_series))
    return "Data inválida"


@app.route('/sectorial/')
def sectorial(selected_date: str = "2024-02-01"):
    return render_template('sectorial.html',
                           date=selected_date,
                           dates=[str(date).split("T")[0] for date in reversed(dm.data["competênciamov"].unique())
                                  if str(date).split("T")[0] != selected_date],
                           stats=dm.data[dm.data["competênciamov"] == "2024-02-01"].groupby([
                                            "saldomovimentação", "Grupo"
                                        ], as_index=True).sum().to_dict()['graudeinstrução'],
                           plot1=pltr.create_adm_layoff_plot(
                               dm.get_adm_layoffs_series(group="Agropecuária").set_index("competênciamov")),
                           plot2=pltr.create_net_plot(dm.get_net_series(group="Agropecuária"))
                           )


@app.route('/stats/sectorial/adm/<selected_date>')
@app.route('/stats/sectorial/adm/')
def stats_sectorial_adm(selected_date: str = "2024-02-01"):
    return jsonify({key[2]: val for key, val in dm.sectors_stats.items() if key[0] == selected_date and key[1] == 1})


@app.route('/stats/sectorial/layoff/<selected_date>')
@app.route('/stats/sectorial/layoff/')
def stats_sectorial_layoff(selected_date: str = "2024-02-01"):
    return jsonify({key[2]: val for key, val in dm.sectors_stats.items() if key[0] == selected_date and key[1] == -1})

@app.route('/stats/sectorial/net/<selected_date>')
@app.route('/stats/sectorial/net/')
def stats_sectorial_net(selected_date: str = "2024-02-01"):
    net_stats = {}
    for key, val in dm.sectors_stats.items():
        if key[0] == selected_date:
            sector = key[2]
            if sector not in net_stats:
                net_stats[sector] = 0
            if key[1] == 1:
                net_stats[sector] += val
            elif key[1] == -1:
                net_stats[sector] -= val
    return jsonify(net_stats)


@app.route('/plot/<chart_type>/<group>')
@app.route('/plot/<chart_type>')
def update_chart(chart_type: str, group: str = None):
    # Dynamically update the chart based on the selected chart type
    if chart_type == "admlayoff":
        fig = pltr.create_adm_layoff_plot(dm.get_adm_layoffs_series(group=group).set_index("competênciamov"))
    # Default
    else:
        fig = pltr.create_net_plot(dm.get_net_series(group=group))

    return jsonify({'plot_html': fig})


if __name__ == "__main__":
    app.run(debug=True)
