import os
from dump_function import dump  # 假设你的 dump 函数在一个叫 dump_function.py 的文件里

def convert_ncm_to_mp3(source_dir='./source', output_dir='./output'):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历 source 目录中的所有 ncm 文件
    for filename in os.listdir(source_dir):
        if filename.endswith('.ncm'):
            input_path = os.path.join(source_dir, filename)
            # 定义输出路径
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.mp3')
            
            print(f"开始转换: {input_path} -> {output_path}")
            # 调用 dump 函数进行转换
            try:
                dump(input_path, output_path=output_path, skip=True, identifier_flag=False)
                print(f"转换成功: {output_path}")
            except Exception as e:
                print(f"转换失败: {input_path} 错误: {e}")

if __name__ == '__main__':
    convert_ncm_to_mp3()
