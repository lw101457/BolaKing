# coding: utf-8
from sqlalchemy import Column, DateTime, String, TIMESTAMP, Table, text
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_prize = Table(
    'prize', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('name', VARCHAR(255), nullable=False, comment='奖品名称'),
    Column('image', String(255), nullable=False, comment='产品略缩图'),
    Column('create_time', TIMESTAMP, nullable=False, comment='添加时间', server_default=text("CURRENT_TIMESTAMP"))
)


t_prize_send_logistics = Table(
    'prize_send_logistics', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('record_id', INTEGER(11), nullable=False, comment='记录id'),
    Column('receiver_id', INTEGER(11), nullable=False, comment='收货人id'),
    Column('status', INTEGER(11), comment='收货状态'),
    Column('logistics_no', String(255), nullable=False, comment='物流单号'),
    Column('company', String(255), nullable=False, comment='物流公司'),
    Column('status_img', String(255), nullable=False, comment='状态图片'),
    Column('detail', VARCHAR(255), nullable=False, comment='物流详情'),
    Column('sender_mobile', String(255), nullable=False, comment='派发员手机号码', server_default=text("'0'")),
    Column('create_time', TIMESTAMP, nullable=False, comment='物流更新时间', server_default=text("CURRENT_TIMESTAMP"))
)


t_prize_send_record = Table(
    'prize_send_record', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('prize_id', INTEGER(11), nullable=False, comment='奖品ID'),
    Column('receiver_id', INTEGER(11), nullable=False, comment='中奖者ID'),
    Column('obtain_time', TIMESTAMP, nullable=False, comment='获奖时间', server_default=text("CURRENT_TIMESTAMP")),
    Column('status', INTEGER(11), nullable=False, comment='派发状态', server_default=text("'0'")),
    Column('receiver_addr', String(255), nullable=False, comment='收货者填写地址'),
    Column('actual_addr', String(255), nullable=False, comment='实际签数地址', server_default=text("''"))
)


t_sys_config = Table(
    'sys_config', metadata,
    Column('user_clause', VARCHAR(255), nullable=False, comment='用户条例条款'),
    Column('privacy_policy', VARCHAR(255), nullable=False, comment='隐私政策'),
    Column('about_us', VARCHAR(255), nullable=False, comment='关于我们')
)


t_sys_notice_type = Table(
    'sys_notice_type', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('title', VARCHAR(255), nullable=False, comment='通知标题内容'),
    Column('image', VARCHAR(255), nullable=False, comment='通知图片'),
    Column('create_time', TIMESTAMP, nullable=False, comment='添加时间', server_default=text("CURRENT_TIMESTAMP"))
)


t_user_announce_count = Table(
    'user_announce_count', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('user_id', INTEGER(11), nullable=False),
    Column('daily', INTEGER(11), nullable=False, comment='日榜次数', server_default=text("'0'")),
    Column('weekly', INTEGER(11), nullable=False, comment='周榜次数', server_default=text("'0'")),
    Column('monthly', INTEGER(11), nullable=False, comment='月榜次数', server_default=text("'0'"))
)


t_user_feedback = Table(
    'user_feedback', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('user_id', INTEGER(11), nullable=False),
    Column('category', VARCHAR(255), nullable=False, comment='类型'),
    Column('content', String(255), nullable=False, comment='反馈内容'),
    Column('contant_no', String(255), nullable=False, comment='联系方式')
)


t_user_info = Table(
    'user_info', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='主键'),
    Column('nickname', String(255), nullable=False, comment='昵称'),
    Column('email', String(255), nullable=False, comment='邮箱', server_default=text("''")),
    Column('mobile', VARCHAR(255), nullable=False, comment='电话号码', server_default=text("''")),
    Column('birthday', INTEGER(11), nullable=False, comment='生日', server_default=text("'0'")),
    Column('wechat', String(255), nullable=False, comment='微信号码', server_default=text("''")),
    Column('qq', INTEGER(13), nullable=False, comment='qq号码', server_default=text("'0'")),
    Column('family_addr', String(255), nullable=False, comment='家庭住址', server_default=text("''")),
    Column('head_image', VARCHAR(255), nullable=False, comment='用户头像', server_default=text("'http://static.leying.me/my-BallKing/app_log.png'")),
    Column('real_name', String(255), nullable=False, comment='用户真实姓名', server_default=text("''")),
    Column('invite_code', VARCHAR(255), nullable=False, comment='邀请码', server_default=text("''")),
    Column('inviter_code', VARCHAR(255), nullable=False, comment='所属邀请人邀请码', server_default=text("''")),
    Column('invite_total', INTEGER(11), nullable=False, comment='邀请成功统计', server_default=text("'0'")),
    Column('quiz_win_total', INTEGER(11), nullable=False, comment='竞猜胜利总数', server_default=text("'0'")),
    Column('quiz_total', INTEGER(11), nullable=False, comment='竞猜总数', server_default=text("'0'")),
    Column('sign_in_total', INTEGER(11), nullable=False, comment='签到总次数', server_default=text("'0'")),
    Column('open_id', String(255), nullable=False, comment='小程序用户openId', server_default=text("''")),
    Column('create_time', TIMESTAMP, nullable=False, comment='创建时间', server_default=text("CURRENT_TIMESTAMP"))
)


t_user_invite = Table(
    'user_invite', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='主键'),
    Column('user_id', INTEGER(11), nullable=False, comment='用户ID'),
    Column('channel', INTEGER(11), nullable=False, comment='邀请分享渠道'),
    Column('stage', INTEGER(11), nullable=False, comment='分享阶段', server_default=text("'0'")),
    Column('share_id', INTEGER(11), nullable=False, comment='对应的分享id'),
    Column('create_time', TIMESTAMP, nullable=False, comment='创建时间', server_default=text("CURRENT_TIMESTAMP")),
    Column('update_time', TIMESTAMP, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
)


t_user_notice = Table(
    'user_notice', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('user_id', INTEGER(11), nullable=False),
    Column('notice_type_id', INTEGER(11), nullable=False, comment='通知类型ID'),
    Column('full_text_url', String(255), nullable=False, comment='全文链接')
)


t_user_quiz_record = Table(
    'user_quiz_record', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='主键'),
    Column('user_id', INTEGER(11), nullable=False),
    Column('match', VARCHAR(255), nullable=False, comment='参与的比赛对场次'),
    Column('quiz_amount', INTEGER(255), nullable=False, comment='下注数量'),
    Column('odds', VARCHAR(255), nullable=False, comment='比赛赔率 ', server_default=text("''")),
    Column('score', VARCHAR(255), nullable=False, comment='结果比分'),
    Column('quiz_choose', VARCHAR(255), nullable=False, comment='我的竞猜选择'),
    Column('expect_earn', INTEGER(11), nullable=False, comment='预计获得盈利'),
    Column('actual_earn', INTEGER(11), nullable=False, comment='获得盈利'),
    Column('status', INTEGER(11), nullable=False, comment='竞猜状态'),
    Column('create_time', TIMESTAMP, nullable=False, comment='创建时间', server_default=text("CURRENT_TIMESTAMP")),
    Column('update_time', DateTime, nullable=False, server_default=text("'1980-01-01 00:00:00'"))
)


t_user_share = Table(
    'user_share', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('user_id', INTEGER(11), nullable=False),
    Column('channel', INTEGER(11), nullable=False, comment='分享渠道'),
    Column('share_type', INTEGER(11), nullable=False, comment='分享类型'),
    Column('create_time', TIMESTAMP, nullable=False, comment='创建时间', server_default=text("CURRENT_TIMESTAMP"))
)


t_user_sign_in_log = Table(
    'user_sign_in_log', metadata,
    Column('id', INTEGER(11), primary_key=True),
    Column('user_id', INTEGER(11), nullable=False),
    Column('create_time', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
)


t_betting_record = Table(
    'betting_record',metadata,
    Column('id',INTEGER(11),primary_key=True,comment='主键'),
    Column('betting_sceen_id',INTEGER(11),nullable=False,comment='竞猜场次id'),
    Column('betting_time',VARCHAR(11),nullable=False,comment='竞猜的时间'),
    Column('betting_moneys',INTEGER(5),nullable=False,comment='投注的金币量'),
    Column('betting_result',VARCHAR(5),nullable=False,comment='竞猜的结果')
)