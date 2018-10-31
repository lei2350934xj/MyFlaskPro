function createCode(codeArea, u_host, u_api, u_method, u_userAgent, u_cookies){
	// 
	console.log('调用commons.js成功');	
}

 	// from locust import HttpLocust, TaskSet, task, events
	// class UserBehavior(TaskSet):

	//     @task(1)
	//     def index_Task(self):
	//         User_Agent = 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6000 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 9)'
	//         cookies = 'BAIDUCUID=_uHa8_uqSu0xiHtj_O2q80awSa0fu2uZ_aSAf_iC2iiXu283gP2pi_aS28gda2f1A; BAIDUID=47264BD0B1D8FCFAE5130645B45F7FB0:FG=1; BDUSS=VBrVno1SWQ0ZnNXU3ExSGd-RGlsTHlMeHdUSXdlb1RrMW9henE0TnBIYVZ4TFZiQUFBQUFBJCQAAAAAAAAAAAEAAAD0peYdbGVpMjM1MDkzNHhqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJU3jluVN45be; WISE_HIS_PM=1; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; BAIDULOC=12944373_4845260_15_131_1539572110677'
	//         with self.client.get('/activity/worldconf/index',headers={'User-Agent':User_Agent,'Cookie':cookies}) as response:
	//             print(response.text)

	// class BaiduUser(HttpLocust):
	//     task_set = UserBehavior
	//     min_wait = 50
	//     max_wait = 50
	//     host='http://cp01-huoye.epc.baidu.com:8090'		