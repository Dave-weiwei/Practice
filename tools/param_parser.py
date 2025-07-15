import ast
import re
import keyword

def extract_parametrize_block(code):
    pattern = re.compile(r"@pytest\.mark\.parametrize\((.+?),\s*\[(.*?)\]\)", re.DOTALL)
    matches = pattern.findall(code)
    return matches

def preprocess_code(code):
    """將 By.ID、By.CSS_SELECTOR 等轉為字串"""
    return (code
        .replace("By.ID", '"id"')
        .replace("By.CLASS_NAME", '"class name"')
        .replace("By.CSS_SELECTOR", '"css selector"')
        .replace("By.LINK_TEXT", '"link text"')
        .replace("By.NAME", '"name"')
        .replace("By.XPATH", '"xpath"')
        .replace("By.TAG_NAME", '"tag name"')
        .replace("By.PARTIAL_LINK_TEXT", '"partial link text"'))

def parse_param_block(block, arg_str):
    arg_names = [x.strip() for x in arg_str.strip("\"'").split(",")]
    block = f"[{block}]"  # 讓它變成合法列表
    node = ast.parse("params = " + block).body[0].value

    items = []
    for param in node.elts:
        values = [ast.literal_eval(arg) for arg in param.args]
        item = dict(zip(arg_names, values))
        for kw in param.keywords:
            if kw.arg == "id":
                item["id"] = ast.literal_eval(kw.value)
        items.append(item)
    return items

def parse_parametrize_code(code, json_key="test_data"):
    blocks = extract_parametrize_block(code)
    if not blocks:
        raise ValueError("未找到 @pytest.mark.parametrize 區塊")
    all_data = {}
    for args, param_block in blocks:
        data = parse_param_block(param_block, args)
        all_data[json_key] = data  # 目前只轉第一組
        break
    return all_data

def filename_to_key(filename):
    name = filename.rsplit(".", 1)[0]
    name = re.sub(r"[^a-zA-Z0-9]+", "_", name)
    if keyword.iskeyword(name):
        name += "_data"
    return name.lower()