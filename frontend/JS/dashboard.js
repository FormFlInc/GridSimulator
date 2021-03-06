
let graphMan = new graphManager();

let label = [-4.5,-4.0,-3.5,-3.0,-2.5,-2,-1.5,-1.0,-0.5,0];


setTimeout(
    function(){
        graphMan.load_graph(array_graphID);
    },1000
)



function getDashboardData(){
    queryHandler.sendRequest("getGraphData",JSON.stringify(array_graphID),graphUpdater.update,graphMan);
    queryHandler.sendRequest("getSummary",simId,setSummary);
    queryHandler.sendRequest("getLog",simId,addLog);
}

function setSummary(data){

    data = JSON.parse(data)

    $("#time_field").text("Time : "+parseFloat(data[0]).toFixed(2))
    $("#hour_field").text("Hour : "+(data[1])+"h")
    $("#sun_field").text("Sun : "+parseFloat(data[2]).toFixed(2)+"%")
    $("#wind_field").text("Wind : "+parseFloat(data[3].toFixed(2))+"%")

    let prd_graph_data = graphMan.getGraph("prd_all_PWR_"+simId).data.datasets[0].data
    let prd = prd_graph_data[prd_graph_data.length-1];
    
    let cns_graph_data = graphMan.getGraph("cns_all_"+simId).data.datasets[0].data
    let cns = cns_graph_data[cns_graph_data.length-1];

    let bill = prd-cns
    
    $("#bill_field").text("Bill : "+bill.toFixed(2)+"MW")
    $("#prd_field").text("Production : "+parseFloat(prd).toFixed(2)+"MW")
    $("#cns_field").text("Consumption : "+parseFloat(cns).toFixed(2)+"MW")
}

function addLog(data){
    data = JSON.parse(data)

    let cur_text = $("#logPanel").html()

    for(let i = 0; i < data.length;i++){
        cur_text += "<p>" + data[i]["message"] + "</p>";
    }

    $("#logPanel").html(cur_text)
    $("#logPanel").animate({ scrollTop: $('#logPanel').prop("scrollHeight")}, 100);

    //console.log(data)
}

timerFunction.push(getDashboardData);

chart = createTreantJs(nodeArray,"#tree-simple")

function nodeClick(params) {

    let cur_node = getNode(nodeArray,params);

    if(cur_node["enable"]==0){
        cur_node["enable"] = 1;

        $("#"+params).css("background-color", "var(--Accent)");

        queryHandler.sendRequest("enable",params,callback);
    }else{
        cur_node["enable"] = 0;
        $("#"+params).css("background-color", "var(--Selected)");

        queryHandler.sendRequest("disable",params,callback);
    }

}

function callback(){}