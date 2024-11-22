# Imports
from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats
import folium

# --------------------------------------------
# Import icons as you like
# --------------------------------------------
# add favicons to your requirements.txt 
# and install to active project virtual environment

UPDATE_INTERVAL_SECS: int = 3

# --------------------------------------------
# Initialize a REACTIVE VALUE with a common data structure
# The reactive value is used to store state (information)
# Used by all the display components that show this live data.
# This reactive value is a wrapper around a DEQUE of readings
# --------------------------------------------

DEQUE_SIZE: int = 5
DEQUE_SIZE: int = 5

# Initialize reactive value
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

# Reactive calculation
@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(-40, -20), 1)  # More realistic Antarctic temperatures
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_dictionary_entry = {"temp": temp, "timestamp": timestamp}
    reactive_value_wrapper.get().append(new_dictionary_entry)
    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)
    return deque_snapshot, df, new_dictionary_entry

# Define the Shiny UI Page layout
# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI
# UI Definition

ui.page_opts(title="PyShiny Express: Antarctic Explorer", fillable=True)


# Sidebar is typically used for user interaction/information
# Note the with statement to create the sidebar followed by a colon
# Everything in the sidebar is indented consistently

with ui.layout_sidebar():
    with ui.sidebar(open="open", width=300):
        ui.h2("Antarctic Explorer", class_="text-center")
        ui.p("Real-time temperature readings in Antarctica.", class_="text-center")
        ui.hr()
        ui.h6("Links:")
        ui.a("GitHub Source", href="https://github.com/denisecase/cintel-05-cintel", target="_blank")
        ui.a("GitHub App", href="https://denisecase.github.io/cintel-05-cintel/", target="_blank")
        ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
        ui.a("PyShiny Express", href="https://shiny.posit.co/blog/posts/shiny-express/", target="_blank")

    with ui.layout_columns(fill=True):
        with ui.value_box(theme="bg-gradient-blue-purple", full_screen=True):
            "Current Temperature"
            @render.text
            def display_temp():
                _, _, latest_dictionary_entry = reactive_calc_combined()
                return f"{latest_dictionary_entry['temp']} °C"

        with ui.value_box(theme="bg-gradient-blue-purple", full_screen=True):
            "Current Date and Time"
            @render.text
            def display_time():
                _, _, latest_dictionary_entry = reactive_calc_combined()
                return f"{latest_dictionary_entry['timestamp']}"

    with ui.card(full_screen=True):
        ui.card_header("Recent Temperature Readings")
        @render.data_frame
        def display_df():
            _, df, _ = reactive_calc_combined()
            pd.set_option('display.width', None)
            return render.DataGrid(df, width="100%")

    with ui.layout_columns(fill=True):
        with ui.card(full_screen=True):
            ui.card_header("Temperature Trend")
            @render_plotly
            def display_plot():
                _, df, _ = reactive_calc_combined()
                if not df.empty:
                    df["timestamp"] = pd.to_datetime(df["timestamp"])
                    fig = px.scatter(df,
                        x="timestamp",
                        y="temp",
                        title="Temperature Readings with Trend Line",
                        labels={"temp": "Temperature (°C)", "timestamp": "Time"},
                        color_discrete_sequence=["blue"])
                    
                    x_vals = range(len(df))
                    y_vals = df["temp"]
                    slope, intercept, _, _, _ = stats.linregress(x_vals, y_vals)
                    df['trend_line'] = [slope * x + intercept for x in x_vals]
                    fig.add_scatter(x=df["timestamp"], y=df['trend_line'], mode='lines', name='Trend Line')
                    fig.update_layout(xaxis_title="Time", yaxis_title="Temperature (°C)")
                    return fig
                return px.scatter()

        with ui.card(full_screen=True):
            ui.card_header("McMurdo Station Location")
            @render.ui
            def render_map():
                m = folium.Map(location=[-90, 0], zoom_start=3, 
                               min_zoom=1, max_zoom=10,
                               tiles='CartoDB positron')
                
                folium.Marker(
                    [-77.85, 166.67],  # McMurdo Station coordinates
                    popup="McMurdo Station",
                    tooltip="Temperature Sensor Location"
                ).add_to(m)
                
                folium.Circle(
                    [-77.85, 166.67],
                    radius=50000,  # 50 km radius
                    color="red",
                    fill=True,
                    fillColor="red"
                ).add_to(m)
                
                m.fit_bounds([[-90, -180], [-60, 180]])
                
                return ui.HTML(m._repr_html_())
