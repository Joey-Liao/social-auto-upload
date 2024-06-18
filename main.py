from conf import BASE_DIR
from pathlib import Path
from upload_video_to_bilibili import upload_video_to_bilibili
from upload_video_to_douyin import upload_video_to_douyin
from upload_video_to_tencent import upload_video_to_tencent
from upload_video_to_xhs import upload_video_to_xhs

filepath = Path(BASE_DIR) / "videos"
account_file_bilibili = Path(BASE_DIR / "bilibili_uploader" / "account.json")
account_file_douyin = Path(BASE_DIR / "douyin_uploader" / "account.json")
account_file_tencent = Path(BASE_DIR / "tencent_uploader" / "account.json")

num_for_day=2
daily_times=[11,22]
def upload_video():
    # upload_video_to_douyin(filepath, account_file_douyin, num_for_day, daily_times)
     #upload_video_to_bilibili(filepath, account_file_bilibili, num_for_day, daily_times)
     #upload_video_to_tencent(filepath, account_file_tencent, num_for_day, daily_times)
     upload_video_to_xhs(filepath, num_for_day, daily_times)

if __name__ == '__main__':
    upload_video()