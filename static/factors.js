	var form=document.getElementById('form');
	form.addEventListener("submit",sendRequest, false);
	function sendRequest(){
		event.preventDefault();
		var number={};
		number.number=document.getElementById('number').value;
		if(/^\s*\-?[0-9]+\s*$/.test(number["number"])){
			var num=parseInt(number["number"].trim());
			if(num>0 && num <= 999999999999){
				request("/matalyst/numbers/factorization/get", JSON.stringify(number));
				document.getElementById('number').value = "";
			}else{
				document.getElementById("content").innerHTML="<div id='error'>Please Enter a Positive Number.</div>"
			}
		}else{
			document.getElementById("content").innerHTML="<div id='error'>Please Enter Only Integer Numbers (0-9).</div>"
		}
		
	}

	function request(url, number){
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
			if (xhr.readyState === 4 && xhr.status === 200) {
				var txt="";
				var num=JSON.parse(xhr.responseText);
				if (num.status == "OK"){
					txt = "<div id='headings'>Factors of "+num.number+" are : </div>";
					txt += generateTable(num.factorsList);
					txt += "<br/><br/><div id='headings'>Explanation : </div>";
					txt += generateExplanation(num.factorsList);
				}
				else if (num.status == "ERROR"){
					txt="<div id='error'>"+num.error+"</div>";
				}
				document.getElementById("content").innerHTML = txt;
			}
		}
		xhr.open("POST", url, true);
		xhr.send(number);
		document.getElementById("content").innerHTML = "Waiting for response ...";
	}

	function generateTable(numberList){
		var txt="<table id='show_table'><tr>";
		var col=7;
		if(numberList[numberList.length-1]>1000000000){
			col=6;
		}else if(numberList[numberList.length-1]>100000000000000){
			col=5;
		}
		for(var i=0; i<numberList.length; i++){
			if(i>0 && i % col==0){
				txt += "<tr/><tr>";
			}
			txt += "<td class='fdata'>"+numberList[i]+ "</td>";
		}
		txt += "<tr/></table>";
		return txt;
	}
	function generateExplanation(numberList){
		var txt="<table id='explanation_table'><tr>";
		var length=numberList.length;
		for(var i=0; i<length-1; i++){
			if(i>0 && i % 3==0){
				txt += "<tr/><tr>";
			}
			if(numberList[i]>numberList[length-1-i]){
				break;
			}
			txt += "<td>"+numberList[i]+ "</td><td>&nbsp;*&nbsp;</td><td>"+numberList[length-1-i]+"</td><td>&nbsp;=&nbsp;</td><td>"+numberList[length-1]+";&nbsp;&nbsp;&nbsp;</td>";
		}
		txt += "<tr/></table>";
		return txt;
	}
