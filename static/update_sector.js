// update_sector.js

document.addEventListener("DOMContentLoaded", function() {
    // Sectorial buttons
    var btInd = document.getElementById("btn-ind");
    var btAgr = document.getElementById("btn-agro");
    var btCon = document.getElementById("btn-cons");
    var btCom = document.getElementById("btn-comm");
    var btSer = document.getElementById("btn-serv");

    $("#btn-adm").click(function() {
        var selectedDate = document.getElementById("date-dropdown").value;
        $.ajax({
            url: "/stats/sectorial/adm/" + selectedDate,
            type: "GET",
            success: function(response) {
                btInd.innerHTML = "Indústria" + '<br><b>' + response["Indústria"] + '</b>';
                btAgr.innerHTML = "Agropecuária" + '<br><b>' + response["Agropecuária"] + '</b>';
                btSer.innerHTML = "Serviços" + '<br><b>' + response["Serviços"] + '</b>';
                btCon.innerHTML = "Construção" + '<br><b>' + response["Construção"] + '</b>';
                btCom.innerHTML = "Comércio" + '<br><b>' + response["Comércio"] + '</b>';
            },
            error: function(xhr) {
                console.log("Erro ao obter o valor de admissões");
            }
        });
    });

    $("#btn-layoff").click(function() {
        var selectedDate = document.getElementById("date-dropdown").value;
        $.ajax({
            url: "/stats/sectorial/layoff/"  + selectedDate,
            type: "GET",
            success: function(response) {
                btInd.innerHTML = "Indústria" + '<br><b>' + response["Indústria"] + '</b>';
                btAgr.innerHTML = "Agropecuária" + '<br><b>' + response["Agropecuária"] + '</b>';
                btSer.innerHTML = "Serviços" + '<br><b>' + response["Serviços"] + '</b>';
                btCon.innerHTML = "Construção" + '<br><b>' + response["Construção"] + '</b>';
                btCom.innerHTML = "Comércio" + '<br><b>' + response["Comércio"] + '</b>';
            },
            error: function(xhr) {
                console.log("Erro ao obter o número de desligamentos");
            }
        });
    });

    $("#btn-net").click(function() {
        var selectedDate = document.getElementById("date-dropdown").value;
        $.ajax({
            url: "/stats/sectorial/net/" + selectedDate,
            type: "GET",
            success: function(response) {
                btInd.innerHTML = "Indústria" + '<br><b>' + response["Indústria"] + '</b>';
                btAgr.innerHTML = "Agropecuária" + '<br><b>' + response["Agropecuária"] + '</b>';
                btSer.innerHTML = "Serviços" + '<br><b>' + response["Serviços"] + '</b>';
                btCon.innerHTML = "Construção" + '<br><b>' + response["Construção"] + '</b>';
                btCom.innerHTML = "Comércio" + '<br><b>' + response["Comércio"] + '</b>';
            },
            error: function(xhr) {
                console.log("Erro ao obter o valor de saldo 2");
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var buttons = [
        document.getElementById('btn-adm'),
        document.getElementById('btn-layoff'),
        document.getElementById('btn-net')
    ];

    var selected = document.getElementById('btn-net');

    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            if (selected !== null) {
                selected.classList.remove('btn-primary');
                selected.classList.add('btn-outline-primary');
            }

            this.classList.remove('btn-outline-primary');
            this.classList.add('btn-primary');

            selected = this;
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var buttonsSectors = [
        document.getElementById("btn-ind"),
        document.getElementById("btn-agro"),
        document.getElementById("btn-cons"),
        document.getElementById("btn-comm"),
        document.getElementById("btn-serv")
    ];

    var selectedSector = document.getElementById("btn-agro");

    buttonsSectors.forEach(function(button) {
        button.addEventListener("click", function() {
            if (selectedSector !== null) {
                selectedSector.classList.remove('btn-primary');
                selectedSector.classList.add('btn-outline-primary');
            }

            this.classList.remove('btn-outline-primary');
            this.classList.add('btn-primary');

            selectedSector = this;
        });
    });
});

var lastSelectedGroup = 'Agropecuária';
function updateChart(event, group) {
    // Check if the selected chart type is the same as the last selected one
    if (group === lastSelectedGroup) {
        console.log('Same group, no update needed');
        return false;
    }
    lastSelectedGroup = group;

    $.ajax({
        url: `/plot/admlayoff/${group}`,
        type: 'GET',
        success: function(data) {
            $('#chart1').html(data.plot_html);
        },
        error: function(xhr, status, error) {
            console.error('Error updating chart:', status, error);
        }
    });

    $.ajax({
        url: `/plot/net/${group}`,
        type: 'GET',
        success: function(data) {
            $('#chart2').html(data.plot_html);
        },
        error: function(xhr, status, error) {
            console.error('Error updating chart:', status, error);
        }
    });
}

var lastSelected = '2024-02-01';
function updateSectorPage() {
    var selection = document.getElementById("date-dropdown").value;
    if (selection === lastSelected) {
        console.log('No update needed');
        return false;
    }
    lastSelected = selection;
    window.location.href = '/stats/sectorial/'+ category + '/' + selection ; // Isso vai redirecionar para /opcao1 ou /opcao2
}