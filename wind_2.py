import streamlit as st
import pandas as pd
# 网页基本设置
st.set_page_config(page_title="风机智慧运维平台",page_icon="⚡",layout="wide")# 网页标题、图表、网页布局（宽屏）
# 侧边菜单栏
st.sidebar.title("⚡ 运维管理系统")# 菜单标题，sidebar提供侧边栏对象
page = st.sidebar.radio("功能菜单",["运行总览", "风机管理", "故障记录"])# 功能选项栏，ratio 创建菜单
st.sidebar.divider()# 分隔线 divider 添加分隔线
st.sidebar.caption("风电智慧运维平台 v1.0")# caption()：显示较小、较次要的说明文字
# 页面标题
st.title("⚡ 风机智慧运维大屏")# title 网页大标题
st.caption("WIND FARM INTELLIGENT OPERATION & MAINTENANCE")
# 设置左侧菜单三个页面page
# 运行总览页面
if page == "运行总览":
    # 指标卡片
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("风机总数", "128 台")
    col2.metric("正常运行", "120 台")
    col3.metric("实时功率", "86.5 MW")
    col4.metric("故障风机", "8 台")
    st.divider()
    # 功率趋势图
    left, right = st.columns([2, 1])# 左侧列对象宽度与右侧列对象宽度比是2：1
    #左侧内容
    with left:# with left作用是让下面内容缩进在左侧列里
        st.subheader("风机功率趋势")
        # 创建功率表格
        power_data = pd.DataFrame({"时间": ["08:00", "09:00", "10:00","11:00", "12:00", "13:00","14:00", "15:00"],"功率(MW)": [55, 62, 58, 70, 75, 68, 82, 86.5]
        }).set_index("时间")# pd.DataFrame：创建二维表格数据，set_index是调用DataFrame的set_index()方法，把 "时间" 这一列设置为表格索引。
        st.line_chart(power_data,color="#38BDF8",height=300)# line_chart 折线图
    # 右侧内容
    with right:
        st.subheader("运行情况")
        st.success("正常运行：120 台")# success 显示正常信息（绿色）
        st.warning("待检查：5 台")# warning 显示警告信息（黄色）
        st.error("故障停机：3 台")# error 显示异常信息（红色）
        st.progress(120 / 128)# progress 进度条
        st.caption("风机正常运行比例：93.75%")
    st.divider()
    # 风机状态表格
    st.subheader("风机实时状态")
    # pd.Dataframe（）:把字典转化成二位表格，将st.dataframe,把数据显示成网页表格，use_container_width=Ture,表格尽量占满
    data = pd.DataFrame({"风机编号": ["WT001", "WT002", "WT003","WT004", "WT005"],"运行状态": ["正常", "正常", "故障","正常", "待检查"],"实时功率(MW)": [1.5, 2.0, 0.0, 1.8, 1.2],"风速(m/s)": [8.2, 9.1, 0.0, 7.8, 6.9]})
    st.dataframe(data,use_container_width=True,hide_index=True)# hide_index 隐藏索引编号
# 风机管理页面
elif page == "风机管理":
    st.subheader("风机管理")
    keyword = st.text_input("请输入风机编号",placeholder="例如 WT001")# text_input 创建单行文本输入框，placeholder 是占位提示参数。
    if keyword:
        st.write("当前查询编号：", keyword)
        st.info("这是演示查询，下一步我们将实现真实筛选。")
    st.write("当前管理 128 台风机。")
# 故障记录页面
elif page == "故障记录":
    st.subheader("故障记录")
    fault_data = pd.DataFrame({"风机编号": ["WT003", "WT018", "WT026"],"故障类型": ["温度异常", "振动异常", "通信中断"],"处理状态": ["待处理", "处理中", "待处理"]})
    st.dataframe(fault_data,use_container_width=True,hide_index=True)
# 页脚
st.divider()
st.caption("演示系统 · 当前数据为模拟数据")
