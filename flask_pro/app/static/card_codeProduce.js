window.onload = function(){
	// 引入外部js文件
	function fs(id){
		return document.getElementById(id);
	}

	// tab栏切换
	var btns = document.getElementsByTagName('button');	// menu
	// console.log(btns)
	var cons = fs('leftPart').getElementsByTagName('div');	// left-part的divs
	// console.log(cons);
	for(var i=0; i<btns.length; i++){
		btns[i].index = i;
		btns[i].onclick = function(){
			// console.log(this.className);
			for(var j=0; j<btns.length; j++){
				btns[j].className = 'menu-button-common';
			}
			this.className = 'menu-button-common menu-btn-current';
			for(var k=0; k<cons.length; k++){
				cons[k].style.display = 'none';
			}
			cons[this.index].style.display = 'block';
		}
	}

	// left-part1的btn事件: 1.获取设置的参数 2.在right-part生成对应的代码
	// 一个坑：input中type=submit会出发请求API的 建议type=button即可
	// 二个坑：textarea标签中的内容竟然用value才能取 而不是innerHTML取
	var leftPartCreate = fs('leftPartCreate');
	leftPartCreate.onclick = function(){
		console.log('start create btn');
		// 1.获取设置的参数
		var u_host = cons[0].getElementsByTagName('input')[0].value;
		var u_api = cons[0].getElementsByTagName('input')[1].value;
		var inputs = cons[0].getElementsByTagName('input');
		var u_method;
		for(var i=2; i<5; i++){
			if(inputs[i].checked == true){
				u_method = inputs[i].value;
			}
		}
		var u_userAgent;
		var userAgent = fs('userAgent');
		var selectIndex = userAgent.selectedIndex;	// 拿到下拉框的选项索引 从0开始
		// console.log(selectIndex);
		switch (selectIndex){
			case 0: // android
				u_userAgent = 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6000 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 9)';
				break; 
			case 1: // ios
				u_userAgent = 'ios版本';
				break;
			default: // 默认android
				u_userAgent = '默认';
		}
		var u_cookies = cons[0].getElementsByTagName('textarea')[0].value;		
		
		// 2.right-part的textarea区域展示生成的代码
		var codeArea = $('#codeArea');	// jquery方法
		var tpl = $('#tpl');
		// console.log('6666', tpl);	
		renderHandlebar(codeArea, tpl, u_host, u_api, u_method, u_userAgent, u_cookies)
		// renderHandlebar(codeArea, u_host, u_api, u_method, u_userAgent, u_cookies)

	}

	$('#leftPartReset').click(function(){
		console.log('jquery 点击 reset btn');
	});	

	// handlebars.js 模板渲染
	// 一个坑：compile拼成了 complie
	function renderHandlebar(codeArea, tpl, u_host, u_api, u_method, u_userAgent, u_cookies){
		// console.log(tpl);
		var source = tpl.html();
		console.log(source);
		var template = Handlebars.compile(source);
		// Handlebars.compile(source)
		var context = {
			host: u_host,
			api: u_api,
			method: u_method,
			UserAgent : u_userAgent,
			cookies: u_cookies,
		};
		console.log(context);
		var html = template(context);
		console.log(html);
		codeArea.html(html);
	}
}