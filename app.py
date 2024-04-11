from flask import Flask, render_template, jsonify

import data_manager as dm
import plotter as pltr

app = Flask(__name__)


@app.route('/')
def index():
    return general()


@app.route('/all/<selected_date>')
def general(selected_date: str = "2024-02-01"):
    stats = dm.adm_layoffs[dm.adm_layoffs["competênciamov"] ==
                        selected_date].astype({"competênciamov": str}).to_dict(orient="records")
    if len(stats) > 0:
        return render_template('index.html',
                               date=selected_date,
                               dates=[str(date).split("T")[0] for date in reversed(dm.data["competênciamov"].unique())
                                      if str(date).split("T")[0] != selected_date],
                               # cities=["Paraíba"] + [city for city in dm.cities],
                               stats=stats[0],
                               plot1=pltr.create_adm_layoff_plot(dm.adm_layoffs.set_index("competênciamov")),
                               plot2=pltr.create_net_plot(dm.net))
    return "Data inválida"


@app.route('/sectorial/')
def sectorial(selected_date: str = "2024-02-01"):
    return render_template('sectorial.html',
                           date=selected_date,
                           dates=[str(date).split("T")[0] for date in reversed(dm.data["competênciamov"].unique())
                                  if str(date).split("T")[0] != selected_date],
                           stats=dm.data[dm.data["competênciamov"] == "2024-02-01"].groupby([
                                            "saldomovimentação", "Grupo"
                                        ], as_index=True).sum().to_dict()['graudeinstrução']
                           )


@app.route('/stats/sectorial/adm/<selected_date>')
@app.route('/stats/sectorial/adm/')
def stats_sectorial_adm(selected_date: str = "2024-02-01"):
    return jsonify({key[1]: val for key, val in dm.sectors_stats.items() if key[0] == 1})


@app.route('/stats/sectorial/layoff/<selected_date>')
@app.route('/stats/sectorial/layoff/')
def stats_sectorial_layoff(selected_date: str = "2024-02-01"):
    return jsonify({key[1]: val for key, val in dm.sectors_stats.items() if key[0] == -1})


@app.route('/stats/sectorial/net/<selected_date>')
@app.route('/stats/sectorial/net/')
def stats_sectorial_net(selected_date: str = "2024-02-01"):
    stats = dict()
    for key, val in dm.sectors_stats.items():
        if key[1] not in stats:
            stats[key[1]] = val * key[0]
        else:
            stats[key[1]] += val * key[0]

    return jsonify(stats)


@app.route('/plot/<chart_type>')
def update_chart(chart_type: str):
    # Dynamically update the chart based on the selected chart type

    #if chart_type == 'short_open_close':  # Short Open Close
    #    fig = pltr.create_open_close_short_plot(dm.get_short_time_series(symbol), symbol)
    #else:  # chart_type == 'short_series':
    # Default Short Time Series
    fig = pltr.create_net_plot(dm.net)

    return jsonify({'plot_html': fig})


if __name__ == "__main__":
    app.run(debug=True)
