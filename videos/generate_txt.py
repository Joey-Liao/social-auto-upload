from translate import Translator
import os
import shutil

titles=["鸡蛋大冒险：完美剥壳之旅",
"给鸡蛋脱衣：生鸡蛋壳的奇妙剥法",
"鸡蛋剥壳秀：极致光滑蛋身",
"剥壳大师：生鸡蛋的脱壳秘密",
"轻松剥壳：鸡蛋的美丽蜕变",
"鸡蛋变身记：完美脱壳体验",
"剥壳小能手：生鸡蛋的新生",
"鸡蛋的冒险：从壳中解放",
"蛋壳奇遇记：轻松去壳大揭秘",
"鸡蛋的秘密：剥壳背后的艺术",
"剥壳挑战：鸡蛋的惊喜蜕变",
"鸡蛋剥壳之旅：简单又奇妙",
"给鸡蛋穿衣脱衣：趣味剥壳过程",
"蛋壳脱壳记：剥壳从未如此有趣",
"鸡蛋的变形记：完美剥壳指南",
"剥壳小妙招：鸡蛋的华丽蜕变",
"蛋壳大冒险：轻松剥壳有诀窍",
"鸡蛋的奇妙旅程：从壳中解脱",
"剥壳魔法：鸡蛋的轻松脱壳术",
"鸡蛋的蜕变：趣味剥壳全过程",
"蛋壳大逃亡：剥壳小窍门",
"剥壳故事：鸡蛋的美丽新生",
"鸡蛋脱壳记：完美剥壳小技巧",
"剥壳大揭秘：鸡蛋的奇妙脱壳术",
"蛋壳奇遇：从壳中逃脱的秘密",
"鸡蛋脱壳冒险：剥壳有趣又简单",
"剥壳小魔法：鸡蛋的轻松脱壳",
"鸡蛋的蜕变之旅：剥壳小能手",
"蛋壳大变身：完美剥壳新方法",
"鸡蛋剥壳记：轻松脱壳的小窍门"]

tag="#坚持不懈 #鸡蛋的新衣 #生鸡蛋 #剥鸡蛋 #短视频"

source_folder = r'D:\Git WorkSpace\py WorkSpace\YouDub-webui\videos\j_egg'
destination_folder = r'D:\Git WorkSpace\py WorkSpace\social-auto-upload\videos'
def gen_txt():
    for i in range(len(titles)):
        #如果文件存在，则先删除
        if os.path.exists(f"day{i}.txt"):
            os.remove(f"day{i}.txt")
        f=open(f"day{i}.txt","a",encoding="utf-8")
        f.write(f"{titles[i]}\n")
        f.write(f"{tag}")
        f.close()

def move_and_rename_videos(source_folder, destination_folder):
    video_count = 1
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith('.mp4'):
                source_path = os.path.join(root, filename)
                new_filename = f"day{video_count}.mp4"
                destination_path = os.path.join(destination_folder, new_filename)
                shutil.move(source_path, destination_path)
                video_count += 1


if __name__ == '__main__':
    gen_txt()
    #move_and_rename_videos(source_folder, destination_folder)