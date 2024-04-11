// Function to update the chart based on the selected chart type
var lastSelectedChartType = 'saldo';
var lastClickedButton = document.getElementById('bt-short1');

function updateChart(event, chartType, symbol) {
    // Check if the selected chart type is the same as the last selected one
    if (chartType === lastSelectedChartType) {
        console.log('Same chart type, no update needed');
        return false;
    }
    lastSelectedChartType = chartType;
    $.ajax({
        url: `/plot/${chartType}/${symbol}`,
        type: 'GET',
        success: function(data) {
            $('#chart').html(data.plot_html);
        },
        error: function(xhr, status, error) {
            console.error('Error updating chart:', status, error);
        }
    });
    // Remove the active style from the previously clicked button
    lastClickedButton.classList.remove('active');
    // Add the active style to the current clicked button
    var currentButton = document.getElementById('bt-' + chartType);
    currentButton.classList.add('active');
    // Update the last clicked button
    lastClickedButton = currentButton;
}