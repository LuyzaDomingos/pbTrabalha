import plotly
import plotly.graph_objects as go

import json

layout = dict(
    margin=dict(l=48, r=48, t=16, b=32),
    xaxis=dict(showgrid=True, zeroline=False, gridcolor="rgba(100, 100, 100, 0.4)", tickformat='%b %Y'),
    plot_bgcolor="rgba(0, 0, 0, 0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_family="DIN Alternate",
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="right", x=1),
)


def create_plot(df, columns):
    data = [
        go.Line(
            x=df.index,
            y=df[column]
        ) for column in columns
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def create_net_plot(df):
    fig = go.Figure()

    colors = ["green" if value > 0 else "red" for value in df.values]

    fig.add_trace(go.Bar(
        x=df.index,
        y=df.values,
        name="Saldo",
        marker_color=colors
    ))

    fig.update_layout(**layout)
    fig.update_layout(dict(
        xaxis=dict(zeroline=True),
    ))

    fig.update_traces(
        hovertemplate="<br>".join([
            "%{x}",
            "%{y}"
        ])
    )
    # Convert the plot to HTML
    return fig.to_html(full_html=False)


def create_adm_layoff_plot(df):
    # Plot the graph using Plotly Express
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['admissao'],
        name="Admissões",
        mode=None,
        fill="tozeroy",
        line=dict(color='green')
    ))

    fig.add_trace(go.Scatter(
        x=df.index,
        y=(-1 * df['demissao']),
        name="Desligamentos",
        mode=None,
        fill="tozeroy",
        line=dict(color='red')
    ))

    fig.update_layout(**layout)
    fig.update_layout(dict(
        yaxis=dict(showgrid=True, zeroline=False, gridcolor="rgba(100, 100, 100, 0.4)"),
    ))

    fig.update_traces(
        hovertemplate="<br>".join([
            "%{x}",
            "%{y}"
        ])
    )
    # Convert the plot to HTML
    return fig.to_html(full_html=False)