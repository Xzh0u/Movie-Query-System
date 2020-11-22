from csv import DictReader  # 导入csv文件
import ast  # 用于string转dict

def readMoviesCSV(filename='app/data/list.csv'):
    with open(filename, 'r') as read_obj:
        reader = DictReader(read_obj)
        items = list(reader)
        for i in range(len(items)):
            items[i]["director"] = items[i]["director"].strip('[').strip(
                ']').strip('\'').strip('\'')
            items[i]["score"] = float(items[i]["score"])
            items[i]["rank"] = int(items[i]["rank"])
            items[i]["runtime"] = items[i]["runtime"].strip('[').strip(']').strip(
                '\'').strip('\'')
            items[i]["image_url"] = items[i]["image_url"].strip('[').strip(
                ']').strip('\'').strip('\'')
            items[i]["link"] = ast.literal_eval(items[i]["link"])
            items[i]["introduction"] = ast.literal_eval(items[i]["introduction"])
            items[i]["majors"] = ast.literal_eval(items[i]["majors"])
            items[i]["type"] = ast.literal_eval(items[i]["type"])
        print(items[0])

    return items

