import plotly.express as px
from models.birds import Birds


def plot_nearby_birds(birds: Birds):
    spark_df = birds.dataframe

    spark_df = (
        spark_df
        .select(
            "latitude",
            "longitude",
            "common_name",
            "scientific_name",
            "how_many",
        )
        .dropna(subset=["latitude", "longitude"])
    )

    pdf = spark_df.toPandas()

    fig = px.scatter_mapbox(
        pdf,
        lat="latitude",
        lon="longitude",
        hover_name="common_name",
        hover_data={
            "scientific_name": True,
            "how_many": True,
        },
        zoom=12,
        height=1200,
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=0, b=0),
    )

    fig.write_html('nearby_birds_map.html', auto_open=True)
