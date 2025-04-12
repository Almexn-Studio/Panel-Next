import yagmail
import config

# 连接服务器
yag_server = yagmail.SMTP(user=config.get('email', 'user'), 
                          password=config.get('email', 'password'), 
                          host=config.get('email', 'host'))

def send_email(receiver, subject, contents, attachments=None):
    """发送邮件
    
    Args:
        receiver (str): 收件人邮箱
        subject (str): 邮件主题
        contents (str): 邮件内容
        attachments (list): 附件列表（可选）
    """
    if attachments is None:
        yag_server.send(receiver, subject, contents, attachments)
    else:
        yag_server.send(receiver, subject, contents)

def send_template(receiver, title, template, replace: dict):
    """发送模板邮件
    
    Args:
        receiver (str): 收件人邮箱
        template (str): 模板名称
        replace (dict): 需要替换的键值对字典
    """
    # 构建完整的文件路径
    template_path = f"data/templates/{template}.html"
    with open(template_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 替换模板中的占位符
    for key, value in replace.items():
        content = content.replace(key, value)  
    # 发送邮件
    yag_server.send(receiver, title, content)