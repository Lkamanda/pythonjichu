import random


def get_User_agent():
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.ce1; SV1; AcooBrowser; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727;"
        " Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5;"
        "AOLBuild 4337.35; Windows NT 5.ce1; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64;"
        " x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    return user_agent
