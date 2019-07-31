from model import t_user_info

cate_sql_map = {
    "nickname": "update user_info set nickname = {0} where id = {1}",
    "email": "update user_info set email = {0} where id = {1}",
    "birthday": "update user_info set birthday = {0} where id = {1}",
    "wechat": "update user_info set wechat = {0} where id = {1}",
    "qq": "update user_info set qq = {0} where id = {1}",
    "family_addr": "update user_info set family_addr = {0} where id = {1}",
}
