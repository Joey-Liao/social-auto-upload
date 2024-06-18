from datetime import timedelta

from datetime import datetime
from pathlib import Path

from conf import BASE_DIR


def get_absolute_path(relative_path: str, base_dir: str = None) -> str:
    # Convert the relative path to an absolute path
    absolute_path = Path(BASE_DIR) / base_dir / relative_path
    return str(absolute_path)


def get_title_and_hashtags(filename):
    """
  获取视频标题和 hashtag

  Args:
    filename: 视频文件名

  Returns:
    视频标题和 hashtag 列表
  """

    # 获取视频标题和 hashtag txt 文件名
    txt_filename = filename.replace(".mp4", ".txt")

    # 读取 txt 文件
    with open(txt_filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 获取标题和 hashtag
    splite_str = content.strip().split("\n")
    title = splite_str[0]
    hashtags = splite_str[1].replace("#", "").split(" ")

    return title, hashtags


def generate_schedule_time_next_day(total_videos, videos_per_day, daily_times=None, timestamps=False, start_days=0):
    """
    生成从次日开始的视频上传计划。

    参数:
    total_videos: int
        需要上传的视频总数。
    videos_per_day: int
        每天上传的视频数量。
    daily_times: list, 可选
        每日上传视频的具体时间点（24小时制）。如未提供，将使用默认时间列表。
    timestamps: bool, 可选
        是否以Unix时间戳形式返回计划时间，默认为False，返回datetime对象。
    start_days: int, 可选
        从次日开始上传视频前等待的天数，默认为0，即从次日开始。

    返回:
    list
        所有视频的上传安排时间列表。
    """

    # 检查videos_per_day是否为正整数
    if videos_per_day <= 0:
        raise ValueError("videos_per_day 应为正整数")

    # 如未指定每日发布时间，则使用默认时间列表
    if daily_times is None:
        daily_times = [6, 11, 14, 16, 22]

    # 确保每天上传的视频数量不超过daily_times长度
    if videos_per_day > len(daily_times):
        raise ValueError("videos_per_day 不应超过daily_times的长度")

    # 初始化计划时间列表
    schedule = []
    current_time = datetime.now()

    # 为每部视频计算并添加上传时间到计划列表中
    for video in range(total_videos):
        day = video // videos_per_day + start_days + 1  # 从次日开始
        daily_video_index = video % videos_per_day

        # 计算当前视频的发布时间
        hour = daily_times[daily_video_index]
        time_offset = timedelta(days=day, hours=hour - current_time.hour,
                                minutes=-current_time.minute, seconds=-current_time.second,
                                microseconds=-current_time.microsecond)
        timestamp = current_time + time_offset

        schedule.append(timestamp)

    # 根据需求转换时间格式为Unix时间戳
    if timestamps:
        schedule = [int(time.timestamp()) for time in schedule]

    # 返回视频上传时间计划列表
    return schedule

