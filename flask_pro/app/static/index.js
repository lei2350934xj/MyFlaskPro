// 入口函数
// 因为index.js放在了base.html的head标签中加载 所以需要写入口函数 保证在html加载完成后加载js文件
window.onload = function(){
	function $(id){
		return document.getElementById(id);
	}

	// 四大精选div的按钮事件
	var btn_codeProduce = $('codeProduce');
	btn_codeProduce.onclick = function(){
		// alert('点击了 codeProduce');
		window.location.href = '/card/codeProduce';	// 在当前窗体中打开新的页面
	}
	// 其余三个待写...
}