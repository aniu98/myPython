import re
import requests, os
project_path = os.path.abspath(os.path.dirname(__file__))
video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'video'))
 
 
class VideoSynthesis:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.m3u8_link = 'https://ksv-video-publish-m3u8.cdn.bcebos.com/8f48c84bb1a6a488ced20f0fc3383dfee61096e1_568x320_401000.m3u8'
        self.base_url = 'https://ksv-video-publish-m3u8.cdn.bcebos.com/'
 
    def get_m3u8_link(self):
        # 下载m3u8视频
        m3u8_response = requests.get(url=self.m3u8_link, headers=self.header, verify=False)
        print(m3u8_response.text)
        return m3u8_response
 
    def handle_m3u8_response(self, m3u8_response):
        # 处理m3u8响应
        
        print('\n'.join(['{0}: {1}'.format(item[0], item[1])
                         for item in m3u8_response.__dict__.items()]))
        ts_filename = re.findall('.*?EXTINF:.*?,\n(.*?)\n', m3u8_response.text.replace(' ', '').replace(r'\n', ''))
        print("-------------")
        print(f'tslist: {ts_filename}')
        ts_link_list = []
        for item in ts_filename:
            result_url = self.base_url + item
            ts_link_list.append(result_url)
        print(f'ts_link_list: {ts_link_list}')
        return ts_link_list, ts_filename
 
    def download_ts_video(self, ts_url_list, ts_filename):
        # 通过ts链接下载ts文件
        for i in range(len(ts_url_list)):
            ts_url = ts_url_list[i]
            ts_name = ts_filename[i]
            try:
                response = requests.get(ts_url, stream=True, verify=False)
            except Exception as e:
                print("异常请求：%s" % e.args)
                return
 
            # 在当前目录下创建个video文件夹
            ts_path = project_path + r"\video\{}".format(ts_name)
            with open(ts_path, "wb+") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
        print("TS文件下载完毕！！")
 
    def heBingTsVideo(self):
        # 视频合成
        hebing_path = video_path + r"\m3u8_video.mp4"
        print(hebing_path)
        all_ts = os.listdir(video_path)
        with open(hebing_path, 'wb+') as f:
            for i in range(len(all_ts)):
                ts_video_path = os.path.join(video_path, all_ts[i])
                f.write(open(ts_video_path, 'rb').read())
        print("合并完成！！")
 
    def run(self):
        m3u8_response = self.get_m3u8_link()
        
        ts_link_list, ts_filename = self.handle_m3u8_response(m3u8_response)
        
        # ts_link_list = ['https://v.pinimg.com/videos/v2/hls/49/3e/6b/493e6bb3f832caf2bef872d648698ff4_hls480w00000.ts', 'https://v.pinimg.com/videos/v2/hls/49/3e/6b/493e6bb3f832caf2bef872d648698ff4_hls480w00001.ts', 'https://v.pinimg.com/videos/v2/hls/49/3e/6b/493e6bb3f832caf2bef872d648698ff4_hls480w00002.ts', 'https://v.pinimg.com/videos/v2/hls/49/3e/6b/493e6bb3f832caf2bef872d648698ff4_hls480w00003.ts']
        # ts_filename = ['493e6bb3f832caf2bef872d648698ff4_hls480w00000.ts', '493e6bb3f832caf2bef872d648698ff4_hls480w00001.ts' ,'493e6bb3f832caf2bef872d648698ff4_hls480w00002.ts', '493e6bb3f832caf2bef872d648698ff4_hls480w00003.ts']
        
        self.download_ts_video(ts_link_list, ts_filename)
        self.heBingTsVideo()
 
 
if __name__ == '__main__':
    video_synthesis = VideoSynthesis()
    video_synthesis.run()
