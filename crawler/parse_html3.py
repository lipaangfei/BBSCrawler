import re
import time
from datetime import datetime

from bs4 import BeautifulSoup, soup

html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<title>面试 - 毕马威(KPMG) 2021校园招聘 -  应届生求职招聘论坛</title>

<meta name="keywords" content="毕马威(KPMG)2021校园招聘,校园招聘" />
<meta name="description" content="毕马威(KPMG)2021校园招聘讨论区，为你解答毕马威(KPMG)2021校园招聘流程、毕马威(KPMG)2021校园招聘网申、毕马威(KPMG)2021校园招聘笔试、毕马威(KPMG)2021校园招聘面试、毕马威(KPMG)2021校园招聘offer发放、毕马威(KPMG)2021校园招聘录取入职等详细问题，另有大量毕马威(KPMG)2021校园招聘综合经验分享，祝广大2015届应届生顺利入职毕马威(KPMG)2021校园招聘; ,应届生求职招聘论坛" />
<meta name="generator" content="Discuz! X3.2" />
<meta name="author" content="Discuz! Team and Comsenz UI Team" />
<meta name="copyright" content="2001-2013 Comsenz Inc." />
<meta name="MSSmartTagsPreventParsing" content="True" />
<meta http-equiv="MSThemeCompatible" content="Yes" />
<base href="" /><link rel="stylesheet" type="text/css" href="data/cache/style_10_common.css?jN8" /><link rel="stylesheet" type="text/css" href="data/cache/style_10_forum_forumdisplay.css?jN8" /><script type="text/javascript">var STYLEID = '10', STATICURL = 'https://bbsimg.yingjiesheng.net/static/', IMGDIR = 'https://bbsimg.yingjiesheng.net/static/image/common', VERHASH = 'jN8', charset = 'gbk', discuz_uid = '13906980', cookiepre = '2Inh_4553_', cookiedomain = '.bbs.yingjiesheng.com', cookiepath = '/', showusercard = '0', attackevasive = '0', disallowfloat = 'login|sendpm|newthread|reply', creditnotice = '2|应届生币|枚', defaultstyle = '', REPORTURL = 'aHR0cDovL2Jicy55aW5namllc2hlbmcuY29tL2ZvcnVtLnBocD9tb2Q9Zm9ydW1kaXNwbGF5JmZpZD00NTYmZmlsdGVyPXR5cGVpZCZ0eXBlaWQ9NTk0Jm9yZGVyYnk9ZGF0ZWxpbmUlMEE=', SITEURL = 'https://bbs.yingjiesheng.com/', JSPATH = 'static/js/', CSSPATH = 'data/cache/style_', DYNAMICURL = '';</script>
<script src="static/js/common.js?jN8" type="text/javascript"></script>
<meta name="application-name" content="应届生求职招聘论坛" />
<meta name="msapplication-tooltip" content="应届生求职招聘论坛" />
<meta name="msapplication-task" content="name=论坛;action-uri=https://bbs.yingjiesheng.com/forum.php;icon-uri=https://bbsimg.yingjiesheng.net/static/image/common/bbs.ico" />
<link rel="archives" title="应届生求职招聘论坛" href="https://bbs.yingjiesheng.com/archiver/" />
<link rel="stylesheet" id="css_widthauto" type="text/css" href="data/cache/style_10_widthauto.css?jN8" />
<script type="text/javascript">HTMLNODE.className += ' widthauto'</script>
<script src="static/js/forum.js?jN8" type="text/javascript"></script>
</head>

<body id="nv_forum" class="pg_forumdisplay" onkeydown="if(event.keyCode==27) return false;">
<div id="append_parent"></div><div id="ajaxwaitid"></div>

<div id="toptb" class="cl">
<div class="wp">
<div class="z"><a href="http://vip.yingjiesheng.com/app/" target="_blank"  style="color: red">应届生求职网手机APP</a><script type="text/javascript">var _speedMark = new Date();</script></div>
<div class="y">
<div style="float: left;">
<a target="_blank" href="http://www.yingjiesheng.com/" class="tit">应届生求职网首页</a><span class="pipe">|</span> 
<a target="_blank" href="http://www.yingjiesheng.com/commend-fulltime-1.html" class="tit">全职推荐</a><span class="pipe">|</span> 
<a target="_blank" href="http://www.yingjiesheng.com/commend-parttime-1.html" class="tit">实习推荐</a><span class="pipe">|</span> 
<a target="_blank" href="http://my.yingjiesheng.com/xuanjianghui.html" class="tit">宣讲会</a><span class="pipe">|</span> 
<a target="_blank" href="http://www.yingjiesheng.com/industry/" class="tit">行业招聘</a><span class="pipe">|</span> 
<a target="_blank" href="http://s.yingjiesheng.com/result.jsp?keyword=%E5%85%AC%E5%8A%A1%E5%91%98+OR+%E4%BA%8B%E4%B8%9A%E5%8D%95%E4%BD%8D&amp;do=2" class="tit">公务员事业单位</a><span class="pipe">|</span> 
<a target="_blank" href="http://www.yingjiesheng.com/major/" class="tit">分类求职</a><span class="pipe">|</span> 
<a target="_blank" href="http://www.yingjiesheng.com/deadline/" class="tit">网申截止</a><span class="pipe">|</span> 
<a target="_blank" href="http://hotel.yingjiesheng.com/" class="tit">求职旅社</a><span class="pipe">|</span> 
<a target="_blank" href="http://k.yingjiesheng.com/center/" class="tit">更多</a>
</div>

<a href="javascript:;" mce_href="javascript:;" onClick="widthauto(this)" style="display: none;">切换到窄版</a>
</div>
</div>
</div>


<div id="qmenu_menu" class="p_pop " style="display: none;">
<ul><li><a href="https://bbs.yingjiesheng.com/forum.php?mod=guide&view=my" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/thread_b.png) !important">帖子</a></li>
<li><a href="https://bbs.yingjiesheng.com/home.php?mod=space&do=friend" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/friend_b.png) !important">好友</a></li>
<li><a href="https://bbs.yingjiesheng.com/home.php?mod=magic" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/magic_b.png) !important">道具</a></li>
<li><a href="https://bbs.yingjiesheng.com/home.php?mod=medal" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/medal_b.png) !important">勋章</a></li>
<li><a href="https://bbs.yingjiesheng.com/home.php?mod=space&do=favorite&view=me" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/favorite_b.png) !important">收藏</a></li>
<li><a href="https://bbs.yingjiesheng.com/home.php?mod=task" style="background-image:url(https://bbsimg.yingjiesheng.net/static/image/feed/task_b.png) !important">任务</a></li>
</ul>
</div>
<div id="hd">
<div class="wp">
<div class="hdc cl"><h2><a href="./" title="应届生求职招聘论坛"><img src="https://bbsimg.yingjiesheng.net/static/image/common/logo.png" alt="应届生求职招聘论坛" border="0" /></a></h2>

<div id="um">
<div class="avt y"><a href="https://bbs.yingjiesheng.com/space-uid-13906980.html"><img src="https://i.yingjiesheng.com/yjs_ucenter/data/avatar/013/90/69/80_avatar_small.jpg" onerror="this.onerror=null;this.src='https://i.yingjiesheng.com/yjs_ucenter/images/noavatar_small.gif'" /></a></div>
<p>
<strong class="vwmy"><a href="https://bbs.yingjiesheng.com/space-uid-13906980.html" target="_blank" title="访问我的空间">夜沧月</a></strong>
<span id="loginstatus">
<a id="loginstatusid" href="member.php?mod=switchstatus" title="切换在线状态" onclick="ajaxget(this.href, 'loginstatus');return false;" class="xi2"></a>
</span>
<a href="https://bbs.yingjiesheng.com/home.php?mod=space&amp;uid=13906980&amp;do=thread&amp;view=me" title="我的帖子" class="xi2">我的帖子</a><span class="pipe">|</span><a href="https://bbs.yingjiesheng.com/home.php?mod=task" class="xi2">任务</a>


<!--<span class="pipe">|</span><a href="connect.php?mod=config" target="_blank">QQ绑定" /></a>-->

<span class="pipe">|</span><a href="https://bbs.yingjiesheng.com/home.php?mod=spacecp">设置</a>
<span class="pipe">|</span><a href="https://bbs.yingjiesheng.com/home.php?mod=space&amp;do=pm" id="pm_ntc">消息</a>
<span class="pipe">|</span><a href="https://bbs.yingjiesheng.com/home.php?mod=space&amp;do=notice" id="myprompt">提醒</a><span id="myprompt_check"></span>
<span class="pipe">|</span><a href="http://union.yingjiesheng.com/api_logout.php">应届生退出</a>
<span class="pipe">|</span><a href="member.php?mod=logging&amp;action=logout&amp;formhash=34ccfd75">退出</a>
</p>
<p>
<a href="https://bbs.yingjiesheng.com/home.php?mod=spacecp&amp;ac=credit&amp;showcredit=1" id="extcreditmenu" onmouseover="delayShow(this, showCreditmenu);" class="showmenu">积分: 46</a>
<span class="pipe">|</span>用户组: <a href="https://bbs.yingjiesheng.com/home.php?mod=spacecp&amp;ac=usergroup" id="g_upmine" class="xi2" onmouseover="delayShow(this, showUpgradeinfo)">职员</a>
</p>
</div>
</div>

<div id="nv">
<a href="javascript:;" id="qmenu" onmouseover="showMenu({'ctrlid':'qmenu','pos':'34!','ctrlclass':'a','duration':2});">快捷导航</a>
<ul><li id="mn_Na2df" onmouseover="showMenu({'ctrlid':this.id,'ctrlclass':'hover','duration':2})"><a href="http://k.yingjiesheng.com/center/" hidefocus="true" target="_blank"   style="font-weight: bold;color: red">我的</a></li><li id="mn_N34dc" ><a href="/forum-59-1.html" hidefocus="true"  >职业规划</a></li><li id="mn_N0fc6" ><a href="/forum-57-1.html" hidefocus="true"  >综合</a></li><li class="a" id="mn_forum" ><a href="https://bbs.yingjiesheng.com/forum.php" hidefocus="true" title="BBS"  >论坛<span>BBS</span></a></li><li id="mn_N83eb" ><a href="/forum-58-1.html" hidefocus="true"  >简历</a></li><li id="mn_N1531" ><a href="/forum-62-1.html" hidefocus="true"  >网申</a></li><li id="mn_N1367" ><a href="/forum-60-1.html" hidefocus="true"  >笔试</a></li><li id="mn_Na3b9" ><a href="/forum-61-1.html" hidefocus="true"  >面试</a></li><li id="mn_Na1d5" ><a href="/forum-433-1.html" hidefocus="true"  >签约</a></li><li id="mn_Neac8" ><a href="/forum-427-1.html" hidefocus="true"  >薪资</a></li><li id="mn_N3c5b" ><a href="/forum-64-1.html" hidefocus="true"  >户口</a></li><li id="mn_N4e59" ><a href="/index.php?gid=1151" hidefocus="true"  >公务员</a></li><li id="mn_N2828" ><a href="/forum-436-1.html" hidefocus="true"  >大礼包</a></li><li id="mn_Nc64b" ><a href="http://vip.yingjiesheng.com/app/index.html" hidefocus="true" target="_blank"   style="text-decoration: underline;color: red">APP</a></li></ul>
</div>
<ul class="p_pop h_pop" id="mn_Na2df_menu" style="display: none"><li><a href="http://my.yingjiesheng.com/index.php/personal.htm" hidefocus="true" target="_blank" >我的简历</a></li><li><a href="/home.php?mod=space&do=thread&view=me" hidefocus="true" target="_blank" >我的论坛帖子</a></li></ul><div class="p_pop h_pop" id="mn_userapp_menu" style="display: none"></div><div id="mu" class="cl">
</div><div id="scbar" class="cl">
<form method="get" action="http://bbs.yingjiesheng.com/search.php" target="_blank">
        <input type="hidden" name="mod" value="forum" />
        <input type="text" name="srchtxt" id="srchtxt" value="" />
        <input type="submit" name="submit" id="new_search_but" value="" />
</form>
</div>
<ul id="scbar_type_menu" class="p_pop" style="display: none;"><li><a href="javascript:;" rel="curforum" fid="456" >本版</a></li><li><a href="javascript:;" rel="forum" class="curtype">帖子</a></li><li><a href="javascript:;" rel="user">用户</a></li></ul>
<script type="text/javascript">
initSearchmenu('scbar', '');
</script>
</div>
</div>




<div id="wp" class="wp"><style id="diy_style" type="text/css"></style>
<!--[diy=diynavtop]--><div id="diynavtop" class="area"></div><!--[/diy]-->
<div id="pt" class="bm cl">
<div class="z">
<a href="./" class="nvhm" title="首页">应届生求职招聘论坛</a><em>&raquo;</em><a href="https://bbs.yingjiesheng.com/forum.php">论坛</a> <em>&rsaquo;</em> <a href="https://bbs.yingjiesheng.com/forum.php?gid=839">会计师事务所(四大及内资所、CPA)</a><em>&rsaquo;</em> <a href="https://bbs.yingjiesheng.com/forum-456-1.html">毕马威(KPMG)</a></div>
</div>

<div class="wp">
<!--[diy=diy1]--><div id="diy1" class="area"></div><!--[/diy]-->
</div>
<div class="boardnav">
<div id="ct" class="wp cl">

<div class="mn">
<div class="bm bml pbn">
<div class="bm_h cl">
<span class="o"><img id="forum_rules_456_img" src="https://bbsimg.yingjiesheng.net/static/image/common/collapsed_no.gif" title="收起/展开" alt="收起/展开" onclick="toggle_collapse('forum_rules_456')" /></span><span class="y">
<a href="https://bbs.yingjiesheng.com/home.php?mod=spacecp&amp;ac=favorite&amp;type=forum&amp;id=456&amp;handlekey=favoriteforum" id="a_favorite" class="fa_fav" onclick="showWindow(this.id, this.href, 'get', 0);">收藏本版</a>

</span>
<h1 class="xs2">
<a href="https://bbs.yingjiesheng.com/forum-456-1.html">毕马威(KPMG)</a>
<span class="xs1 xw0 i">今日: <strong class="xi1">41</strong><span class="pipe">|</span>主题: <strong class="xi1">32033</strong></span></h1>
</div>
<div class="bm_c cl pbn">
<div>版主: <span class="xi2"><a href="https://bbs.yingjiesheng.com/space-username-karen822.html" class="notabs" c="1">karen822</a>, <a href="https://bbs.yingjiesheng.com/space-username-KPMGHR.html" class="notabs" c="1">KPMGHR</a></span></div><div id="forum_rules_456" style=";">
<div class="ptn xg2"><a href="http://www.yingjiesheng.com/company_jump.php?ID=7" target="_blank"><font color="red"><strong>毕马威2021园招聘求职大礼包——备战毕马威2021校园招聘</strong></font></a> <br />
<font color="blue">本版为毕马威2019校园招聘讨论区，讨论帖全部为2019年新帖和历年精华资料，如果你想浏览之前旧帖，请点击：</font><a href="http://bbs.yingjiesheng.com/forum-2634-1.html" target="_blank"><font color="green">毕马威2008-2018校园招聘旧帖归档区</font></a></div>
</div>
</div>
</div>

<div class="bm bmw fl">
<div class="bm_h cl">
<span class="o"><img id="subforum_456_img" src="https://bbsimg.yingjiesheng.net/static/image/common/collapsed_no.gif" title="收起/展开" alt="收起/展开" onclick="toggle_collapse('subforum_456');" /></span>
<h2>子版块</h2>
</div>

<div id="subforum_456" class="bm_c" style="">
<table cellspacing="0" cellpadding="0" class="fl_tb">
<tr><td>
<h2><a href="https://bbs.yingjiesheng.com/forum-2634-1.html"  style=""><b>毕马威2008-2011校园招聘旧帖归档区</b></a></h2>
</td>
<td class="fl_i">
<span class="xi2"><span title="13279">1万</span></span><span class="xg1"> / <span title="150937">15万</span></span></td>
<td class="fl_by">
<div>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=774128&amp;goto=lastpost#lastpost" class="xi2">case study presentation 时  你 ...</a> <cite>2020-5-10 00:50 <a href="https://bbs.yingjiesheng.com/space-username-wjwjs.html">wjwjs</a></cite>
</div>
</td>
</tr>
<tr class="fl_row">
</tr>
</table>
</div>
</div>


<div class="drag">
<!--[diy=diy4]--><div id="diy4" class="area"></div><!--[/diy]-->
</div>




<div id="pgt" class="bm bw0 pgs cl">
<span id="fd_page_top"><div class="pg"><strong>1</strong><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=4">4</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=5">5</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=6">6</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=7">7</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=8">8</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=9">9</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=10">10</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=155" class="last">... 155</a><label><input type="text" name="custompage" class="px" size="2" title="输入页码，按回车快速跳转" value="1" onkeydown="if(event.keyCode==13) {window.location='forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page='+this.value;; doane(event);}" /><span title="共 155 页"> / 155 页</span></label><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=2" class="nxt">下一页</a></div></span>
<span class="pgb y"  ><a href="https://bbs.yingjiesheng.com/forum.php">返&nbsp;回</a></span>
<a href="javascript:;" id="newspecial" onmouseover="$('newspecial').id = 'newspecialtmp';this.id = 'newspecial';showMenu({'ctrlid':this.id})" onclick="showWindow('newthread', 'forum.php?mod=post&action=newthread&fid=456')" title="发新帖"><img src="https://bbsimg.yingjiesheng.net/static/image/common/pn_post.png" alt="发新帖" /></a></div>
<ul id="thread_types" class="ttp bm cl">
<li id="ttp_all" ><a href="https://bbs.yingjiesheng.com/forum-456-1.html">全部</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=591&orderby=dateline%0A">问答</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=592&orderby=dateline%0A">其他</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=593&orderby=dateline%0A">笔试</a></li>
<li class="xw1 a"><a href="https://bbs.yingjiesheng.com/forum-456-1.html">面试</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=595&orderby=dateline%0A">网申</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=596&orderby=dateline%0A">公司概况</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=597&orderby=dateline%0A">综合经验</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=typeid&amp;typeid=598&orderby=dateline%0A">签约</a></li>
</ul>
<script type="text/javascript">showTypes('thread_types');</script>
<div id="threadlist" class="tl bm bmw" style="position: relative;">
<div class="th">
<table cellspacing="0" cellpadding="0">
<tr>
<th colspan="2">
<div class="tf">
<span id="atarget" onclick="setatarget(-1)" class="y atarget_1" title="在新窗口中打开帖子">新窗</span>						筛选:
<a id="filter_special" href="javascript:;" class="showmenu xi2" onclick="showMenu(this.id)">
全部主题</a>
<a id="filter_dateline" href="javascript:;" class="showmenu xi2" onclick="showMenu(this.id)">
时间</a>
<a id="filter_orderby" href="javascript:;" class="showmenu xi2" onclick="showMenu(this.id)">
最后发表</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=author&amp;orderby=dateline&typeid=594">发帖时间</a>&nbsp;
<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=reply&amp;orderby=replies&typeid=594">回复/查看</a>&nbsp;
<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=lastpost&amp;orderby=lastpost&typeid=594">最后发表</a>
<span class="pipe">|</span><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=digest&amp;digest=1&typeid=594&orderby=dateline%0A" class="xi2">精华</a></div>
</th>
<td class="by">作者</td>
<td class="num">回复/查看</td>
<td class="by">最后发表</td>
</tr>
</table>
</div>
<div class="bm_c">
<script type="text/javascript">var lasttime = 1620878151;</script>
<div id="forumnew" style="display:none"></div>
<form method="post" autocomplete="off" name="moderate" id="moderate" action="forum.php?mod=topicadmin&amp;action=moderate&amp;fid=456&amp;infloat=yes&amp;nopost=yes">
<input type="hidden" name="formhash" value="34ccfd75" />
<input type="hidden" name="listextra" value="page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" />
<table summary="forum_456" cellspacing="0" cellpadding="0">
<tbody id="stickthread_2320369">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320369&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="本版置顶主题 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pin_1.gif" alt="本版置顶" />
</a>
</td>
<th class="common">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320369&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" style="font-weight: bold;color: #8F2A90;" onclick="atarget(this)" class="xst" >2021校园招聘面试经验汇总，供2022校园招聘同学参考</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-443334.html" c="1">吃吃</a></cite>
<em><span>2021-4-19 11:09</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320369&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>1105</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B3%D4%B3%D4.html" c="1">吃吃</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320369&goto=lastpost#lastpost">2021-4-19 11:09</a></em>
</td>
</tr>
</tbody>
<tbody id="separatorline">
<tr class="ts">
<td>&nbsp;</td>
<th>&nbsp;</th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
</tr>
</tbody>
<tbody id="normalthread_2195893">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2195893&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2195893&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG par面后结果</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10865327.html" c="1">sammabon9631</a></cite>
<em><span>2019-3-15 02:42</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2195893&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">4</a><em>27901</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-sammabon9631.html" c="1">sammabon9631</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2195893&goto=lastpost#lastpost">2021-5-13 11:25</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2296847">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG bj 面经</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/filetype/image_s.gif" alt="attach_img" title="图片附件" align="absmiddle" />
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=4">4</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=5">5</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=6">6</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13369092.html" c="1">我有只叫明明的小熊</a></cite>
<em><span>2020-10-31 12:27</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2296847&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">106</a><em>6128</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-hagendasivv.html" c="1">hagendasivv</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2296847&goto=lastpost#lastpost">2021-5-13 11:13</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1897985">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1897985&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1897985&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >M面后多久有par面通知？</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1897985&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-5069895.html" c="1">小莹在努力</a></cite>
<em><span>2014-10-30 17:00</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1897985&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">34</a><em>37127</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-chenyueviola.html" c="1">chenyueviola</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1897985&goto=lastpost#lastpost">2021-5-13 11:12</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2238076">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2238076&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2238076&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >BJ Audit par面后收到offer时间，供大家参考（注意时间从par面算起）</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-11596401.html" c="1">疾风剑豪李白</a></cite>
<em><span>2019-11-14 17:58</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2238076&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">16</a><em>9099</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B6%BA%C4%E3%CD%E6%B6%F9%C4%D8.html" c="1">逗你玩儿呢</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2238076&goto=lastpost#lastpost">2021-5-13 11:03</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321466">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321466&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321466&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >北京2021审计Par面offer情况统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12626432.html" c="1">tongtong12345678</a></cite>
<em><span>2021-4-28 11:25</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321466&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">13</a><em>730</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-flyhappybear.html" c="1">flyhappybear</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321466&goto=lastpost#lastpost">2021-5-13 10:12</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2053451">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2053451&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2053451&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >OT后大概多久能收到M面？</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9270518.html" c="1">omit淇淇淇</a></cite>
<em><span>2016-9-12 23:12</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2053451&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">13</a><em>35041</em></td>
<td class="by">
<cite>本站网友</cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2053451&goto=lastpost#lastpost">2021-5-13 10:06</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322814">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322814&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322814&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >刚收到北京的精英计划面试，有同学收到吗</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322814&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12635007.html" c="1">linglingtime</a></cite>
<em><span>2021-5-12 20:40</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322814&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>97</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-xiangyaozhaoshixi.html" c="1">xiangyaozhaoshixi</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322814&goto=lastpost#lastpost">2021-5-13 09:57</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1059398">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1059398&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1059398&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >二面后多久拿到口头或短信offer （投票）</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1059398&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-3470283.html" c="1">tedlinan</a></cite>
<em><span>2011-11-27 14:29</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1059398&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">38</a><em>41255</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Eddie_zhu.html" c="1">Eddie_zhu</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1059398&goto=lastpost#lastpost">2021-5-13 09:37</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322313">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322313&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322313&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >gz所春招m面后都多久有反馈呀</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322313&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13344246.html" c="1">Sigh___</a></cite>
<em><span>2021-5-7 20:52</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322313&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">12</a><em>202</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-aqlp10.html" c="1">aqlp10</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322313&goto=lastpost#lastpost">2021-5-12 23:17</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_988558">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >大家case一般准备多长时间?[全过程]</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=4">4</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=5">5</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-3530349.html" c="1">wuhaoyu</a></cite>
<em><span>2011-10-23 16:33</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=988558&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">81</a><em>49145</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-378969189.html" c="1">378969189</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=988558&goto=lastpost#lastpost">2021-5-12 19:47</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2003084">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2003084&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2003084&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >重发！sh拿到offer男女比例</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8362481.html" c="1">adaaada</a></cite>
<em><span>2015-11-10 17:47</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2003084&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">3</a><em>25099</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-adaaada.html" c="1">adaaada</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2003084&goto=lastpost#lastpost">2021-5-12 18:53</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2002631">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002631&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002631&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >sh audit 目前拿到offer的 男女比例统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8362481.html" c="1">adaaada</a></cite>
<em><span>2015-11-9 21:08</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002631&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>4974</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B2%DC%B9%B7%B9%B7.html" c="1">曹狗狗</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2002631&goto=lastpost#lastpost">2021-5-12 18:50</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1991694">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >M面你的案例是什么</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=4">4</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=5">5</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-7432095.html" c="1">bei9088</a></cite>
<em><span>2015-10-22 16:15</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1991694&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">87</a><em>43613</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%D6%DC%DF%AE%CF%E8kaye.html" c="1">周弋翔kaye</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1991694&goto=lastpost#lastpost">2021-5-12 18:49</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1574052">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KP M面的Case Study是用中文还是英文？</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=4">4</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-2905705.html" c="1">eyesonkilly</a></cite>
<em><span>2012-10-24 13:43</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1574052&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">63</a><em>62484</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-TailChan.html" c="1">TailChan</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1574052&goto=lastpost#lastpost">2021-5-12 18:49</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2169379">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2169379&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2169379&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >10.20上海审计m面试结果</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8460234.html" c="1">jinwenhui</a></cite>
<em><span>2018-10-21 18:33</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2169379&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>3309</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-jinwenhui.html" c="1">jinwenhui</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2169379&goto=lastpost#lastpost">2021-5-12 18:48</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1911497">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1911497&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1911497&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >北京审计par面用中文还是英文？</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-7611940.html" c="1">rocky1112</a></cite>
<em><span>2014-11-15 11:24</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1911497&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">18</a><em>25566</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Anthony91.html" c="1">Anthony91</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1911497&goto=lastpost#lastpost">2021-5-12 16:57</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2126975">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2126975&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2126975&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >请问今年北京fs金融组par面多大机率遇到全英文呀</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9985673.html" c="1">yitian_piao</a></cite>
<em><span>2017-11-8 20:06</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2126975&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>5947</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-yitian_piao.html" c="1">yitian_piao</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2126975&goto=lastpost#lastpost">2021-5-12 16:56</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2064068">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064068&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064068&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >投北京的留学生获得面试邀请的情况</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9304113.html" c="1">southsoung</a></cite>
<em><span>2016-10-28 04:14</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064068&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>11757</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-southsoung.html" c="1">southsoung</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2064068&goto=lastpost#lastpost">2021-5-12 16:23</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2277449">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2277449&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2277449&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >SZ return offer统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-11107156.html" c="1">zhongke11</a></cite>
<em><span>2020-7-16 20:45</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2277449&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">9</a><em>3643</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-qiqia1234.html" c="1">qiqia1234</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2277449&goto=lastpost#lastpost">2021-5-12 16:22</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322529">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322529&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322529&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG日常实习生申请</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322529&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-11810259.html" c="1">虎斑碳素</a></cite>
<em><span>2021-5-10 14:43</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322529&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">1</a><em>118</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-CynthiaXSS.html" c="1">CynthiaXSS</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322529&goto=lastpost#lastpost">2021-5-12 16:20</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322674">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322674&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322674&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG青岛有面试的消息吗？</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322674&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12228645.html" c="1">笑一个叭</a></cite>
<em><span>2021-5-11 17:46</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322674&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">11</a><em>168</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%C7%EF%CB%AE%B9%B2%B3%A4%CC%EC%D2%BB%C9%AB1204.html" c="1">秋水共长天一色1204</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322674&goto=lastpost#lastpost">2021-5-12 16:01</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2007830">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2007830&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2007830&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >请大家进来帮忙统计一下par面通过率</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8415532.html" c="1">xinmeiqi</a></cite>
<em><span>2015-11-18 08:25</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2007830&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">4</a><em>22297</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Anthony91.html" c="1">Anthony91</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2007830&goto=lastpost#lastpost">2021-5-12 15:35</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322567">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322567&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322567&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >精英计划——大家GBA做完多久收到了面试邀请呀</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322567&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13173320.html" c="1">积极的熊同学</a></cite>
<em><span>2021-5-10 20:13</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322567&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>268</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%BB%FD%BC%AB%B5%C4%D0%DC%CD%AC%D1%A7.html" c="1">积极的熊同学</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322567&goto=lastpost#lastpost">2021-5-12 15:12</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2159053">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2159053&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2159053&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >一般做完OT后多久收到面试通知呢？</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10569887.html" c="1">beth7711</a></cite>
<em><span>2018-8-14 10:14</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2159053&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>20793</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-beth7711.html" c="1">beth7711</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2159053&goto=lastpost#lastpost">2021-5-12 14:45</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2073839">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073839&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073839&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >大家par面完大概多长时间收到offer呢（BJ所）</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9202390.html" c="1">19920510123abc</a></cite>
<em><span>2016-11-21 13:33</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073839&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">3</a><em>17408</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-silkagelx.html" c="1">silkagelx</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2073839&goto=lastpost#lastpost">2021-5-12 13:12</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1920572">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1920572&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1920572&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >offer比较＋分享p面问题</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-7701741.html" c="1">shuizhido</a></cite>
<em><span>2014-11-26 17:04</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1920572&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">10</a><em>16600</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-hzr1226.html" c="1">hzr1226</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1920572&goto=lastpost#lastpost">2021-5-12 13:02</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321188">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321188&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321188&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >求组队mock KPMG群面</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13537440.html" c="1">youngbin6</a></cite>
<em><span>2021-4-25 23:32</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321188&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">6</a><em>252</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-gwogwo.html" c="1">gwogwo</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321188&goto=lastpost#lastpost">2021-5-12 11:05</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322411">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322411&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322411&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >宁波所m面完没消息是不是凉了呀</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322411&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9848476.html" c="1">是星星呀</a></cite>
<em><span>2021-5-8 19:56</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322411&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">4</a><em>210</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-TheCucKoo.html" c="1">TheCucKoo</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322411&goto=lastpost#lastpost">2021-5-12 07:09</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321600">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321600&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321600&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >求教宁波M面的方式</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10599144.html" c="1">fuyou23333</a></cite>
<em><span>2021-4-29 10:55</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321600&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">8</a><em>332</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B1%A7%C3%A8%C2%C3%D0%D0.html" c="1">抱猫旅行</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321600&goto=lastpost#lastpost">2021-5-12 02:11</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2002282">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002282&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002282&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >11.2par面 GZ所收到offer统计</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8265699.html" c="1">anyyf</a></cite>
<em><span>2015-11-9 12:03</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002282&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">10</a><em>3945</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%D0%A1%D0%DC%CE%AC%C4%E1R.html" c="1">小熊维尼R</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2002282&goto=lastpost#lastpost">2021-5-11 22:11</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2300582">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2300582&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2300582&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KP上海所审计，11.2-11.6par面后结果</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12816617.html" c="1">lawanda98</a></cite>
<em><span>2020-11-10 12:02</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2300582&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>1944</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-hzr1226.html" c="1">hzr1226</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2300582&goto=lastpost#lastpost">2021-5-11 22:10</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1913653">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1913653&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1913653&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >想统计一下大家par面时遇到的都是什么样的par，通过率怎么样？</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-4413670.html" c="1">湘雨涵</a></cite>
<em><span>2014-11-18 13:16</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1913653&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">8</a><em>22479</em></td>
<td class="by">
<cite>本站网友</cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1913653&goto=lastpost#lastpost">2021-5-11 22:07</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2213598">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2213598&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2213598&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >2020北京所KP审计offer率统计，截至8.28</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9074223.html" c="1">艾伦铎尔</a></cite>
<em><span>2019-8-28 19:34</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2213598&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">1</a><em>5370</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-uuuuuuuu99.html" c="1">uuuuuuuu99</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2213598&goto=lastpost#lastpost">2021-5-11 21:04</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2298852">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2298852&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2298852&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG深圳审计有收到par面的吗</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10567763.html" c="1">A1079015284</a></cite>
<em><span>2020-11-5 15:46</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2298852&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">12</a><em>1110</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-A1079015284.html" c="1">A1079015284</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2298852&goto=lastpost#lastpost">2021-5-11 21:01</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321487">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321487&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321487&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >【群面】有人想今晚练群面么</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13657297.html" c="1">Jessicain2021</a></cite>
<em><span>2021-4-28 14:23</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321487&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>342</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Jessicain2021.html" c="1">Jessicain2021</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321487&goto=lastpost#lastpost">2021-5-11 15:56</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1937368">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1937368&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1937368&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KP上海只有口头offer但没有后文的来投个票吧</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1937368&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-7647505.html" c="1">Adrian小超</a></cite>
<em><span>2014-12-19 23:26</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1937368&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">30</a><em>31770</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Laura113.html" c="1">Laura113</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1937368&goto=lastpost#lastpost">2021-5-11 09:00</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319171">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319171&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319171&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >毕马威可以线上面试吗</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13759423.html" c="1">menghh55</a></cite>
<em><span>2021-4-7 22:48</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319171&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">10</a><em>771</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-lulu5137.html" c="1">lulu5137</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319171&goto=lastpost#lastpost">2021-5-10 23:19</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2318699">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318699&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318699&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >deal advisory M面+Par面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9695577.html" c="1">Luci171</a></cite>
<em><span>2021-4-7 14:13</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318699&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>857</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-manaG.html" c="1">manaG</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2318699&goto=lastpost#lastpost">2021-5-10 23:17</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321348">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321348&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321348&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >par面后收到offer（希望投票的都是22号以后的哇）</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12626432.html" c="1">tongtong12345678</a></cite>
<em><span>2021-4-27 12:32</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321348&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">3</a><em>459</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-logining.html" c="1">logining</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321348&goto=lastpost#lastpost">2021-5-10 17:55</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320197">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320197&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320197&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >毕马威北京春招</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=2320197&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-11920768.html" c="1">D6666</a></cite>
<em><span>2021-4-17 09:54</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320197&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">24</a><em>1345</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B3%C218839289688.html" c="1">陈18839289688</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320197&goto=lastpost#lastpost">2021-5-10 17:03</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322470">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322470&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322470&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >sz 2021春招4月面试的有收到offer的吗</a>
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322470&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12738532.html" c="1">criszhang</a></cite>
<em><span>2021-5-9 19:36</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322470&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>160</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-ahsdtfguh8.html" c="1">ahsdtfguh8</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322470&goto=lastpost#lastpost">2021-5-10 15:34</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320858">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320858&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320858&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >SH所春招审计有收到面试通知和offer的吗？麻烦报下日期</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13644795.html" c="1">ninghaimeng</a></cite>
<em><span>2021-4-22 16:40</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320858&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">9</a><em>397</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B5%CB%B2%BB%C0%FB%D0%A1%B6%E0.html" c="1">邓不利小多</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320858&goto=lastpost#lastpost">2021-5-10 13:48</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2322503">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322503&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322503&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >2021/4/28 SZ audit 参加面试的朋友们 拿到p面通知了吗</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&amp;tid=2322503&amp;goto=lastpost#lastpost" class="xi1">New</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13801938.html" c="1">害羞土犬冢牙5587</a></cite>
<em><span>2021-5-10 10:29</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2322503&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>96</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%BA%A6%D0%DF%CD%C1%C8%AE%DA%A3%D1%C05587.html" c="1">害羞土犬冢牙5587</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2322503&goto=lastpost#lastpost">2021-5-10 10:29</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320984">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320984&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320984&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >kpmg SZ 春招</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12738532.html" c="1">criszhang</a></cite>
<em><span>2021-4-23 17:38</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320984&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">9</a><em>475</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%BA%A6%D0%DF%CD%C1%C8%AE%DA%A3%D1%C05587.html" c="1">害羞土犬冢牙5587</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320984&goto=lastpost#lastpost">2021-5-10 10:23</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2063125">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2063125&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2063125&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KP 上海审计 10月20号par面后收到offer统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9199527.html" c="1">周周Catherine</a></cite>
<em><span>2016-10-25 19:22</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2063125&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>5314</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-faithzzzzzz.html" c="1">faithzzzzzz</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2063125&goto=lastpost#lastpost">2021-5-9 20:52</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1603650">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1603650&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1603650&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >M面Case presentation时，你用的是中文还是英文？</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1603650&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=1603650&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-1867316.html" c="1">Rm95</a></cite>
<em><span>2012-11-18 10:59</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1603650&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">50</a><em>53966</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-kiterunner2015.html" c="1">kiterunner2015</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1603650&goto=lastpost#lastpost">2021-5-9 14:57</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320474">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320474&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320474&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >毕马威深圳咨询offer</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9758571.html" c="1">melonyliu</a></cite>
<em><span>2021-4-19 19:42</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320474&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>309</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-melonyliu.html" c="1">melonyliu</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320474&goto=lastpost#lastpost">2021-5-9 09:29</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_1763367">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1763367&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1763367&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >统计下有人m面pre用中文吗</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-6245113.html" c="1">huluobotou</a></cite>
<em><span>2013-11-7 21:52</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=1763367&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">12</a><em>14505</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-sherryxu21.html" c="1">sherryxu21</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=1763367&goto=lastpost#lastpost">2021-5-9 00:43</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321373">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321373&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321373&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG广州</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13575935.html" c="1">皮卡丘的丸子</a></cite>
<em><span>2021-4-27 15:17</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321373&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>389</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%C6%A4%BF%A8%C7%F0%B5%C4%CD%E8%D7%D3.html" c="1">皮卡丘的丸子</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321373&goto=lastpost#lastpost">2021-5-8 23:57</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2121467">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2121467&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2121467&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >南京所各岗位【2018】面试情况统计及面试交流</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9970435.html" c="1">weonlyliveonce</a></cite>
<em><span>2017-10-24 12:33</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2121467&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">11</a><em>5712</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-lenaxule.html" c="1">lenaxule</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2121467&goto=lastpost#lastpost">2021-5-8 20:56</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321114">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321114&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321114&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >2021 kpbj春招par面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13866494.html" c="1">时海1999</a></cite>
<em><span>2021-4-25 14:36</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321114&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">14</a><em>635</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%C5%AC%C1%A6%A3%ABN.html" c="1">努力＋N</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321114&goto=lastpost#lastpost">2021-5-8 08:56</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2002548">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002548&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002548&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >成都所收到par面情况统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8414973.html" c="1">N'aix</a></cite>
<em><span>2015-11-9 18:31</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2002548&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>2104</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-N%27aix.html" c="1">N'aix</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2002548&goto=lastpost#lastpost">2021-5-7 13:40</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2317049">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317049&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317049&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >GZ 春招</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12718501.html" c="1">我要拿offerX</a></cite>
<em><span>2021-3-11 15:20</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317049&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">6</a><em>689</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-qweqweppp.html" c="1">qweqweppp</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2317049&goto=lastpost#lastpost">2021-5-6 12:03</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2240637">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2240637&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2240637&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >上海所秋招offer发放情况</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10266923.html" c="1">lllllotty</a></cite>
<em><span>2019-11-20 14:23</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2240637&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">13</a><em>6838</em></td>
<td class="by">
<cite>本站网友</cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2240637&goto=lastpost#lastpost">2021-5-6 11:13</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2064822">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064822&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064822&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG 深圳咨询 M面情况！ 深圳！咨询哟！</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9263300.html" c="1">映昔Amber</a></cite>
<em><span>2016-10-30 10:51</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2064822&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">19</a><em>4907</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-woyaopwcoffer.html" c="1">woyaopwcoffer</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2064822&goto=lastpost#lastpost">2021-5-6 10:31</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321807">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321807&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321807&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" style="color: #8F2A90;" onclick="atarget(this)" class="xst" >二线所-厦门所-暑期实习生群面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13835858.html" c="1">lolhrt</a></cite>
<em><span>2021-4-30 18:58</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321807&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>949</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-zzxjessiez.html" c="1">zzxjessiez</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321807&goto=lastpost#lastpost">2021-5-5 11:41</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2318417">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318417&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318417&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >郑州所Par面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13723703.html" c="1">Deryck</a></cite>
<em><span>2021-3-30 07:55</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318417&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>459</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B4%D6%E1%EE%D2%BB2910%C2%E9%B2%D6%D2%B6.html" c="1">粗犷一2910麻仓叶</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2318417&goto=lastpost#lastpost">2021-5-3 19:03</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319371">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319371&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319371&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG zz所</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13662169.html" c="1">-Divine</a></cite>
<em><span>2021-4-9 17:13</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319371&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">10</a><em>464</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B4%D6%E1%EE%D2%BB2910%C2%E9%B2%D6%D2%B6.html" c="1">粗犷一2910麻仓叶</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319371&goto=lastpost#lastpost">2021-5-3 19:02</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2129231">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2129231&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2129231&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >pre的时候大家是用英文还是中文呢</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-9967168.html" c="1">a751255227@qq.c</a></cite>
<em><span>2017-11-15 11:05</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2129231&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>2784</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-pdxguo.html" c="1">pdxguo</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2129231&goto=lastpost#lastpost">2021-5-3 16:19</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2073509">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073509&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073509&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >成都2017 审计Par面offer情况统计</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8949056.html" c="1">cherylcheryl123</a></cite>
<em><span>2016-11-20 14:54</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2073509&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">16</a><em>4693</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-lnkdywbi.html" c="1">lnkdywbi</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2073509&goto=lastpost#lastpost">2021-4-30 18:59</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_913752">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >大家拿到offer的同学们，都是par面完几天都到的？？谢谢啦，给大家的等待作参考</a>
<span class="tps">&nbsp;...<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A&amp;page=4">4</a></span>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-2005485.html" c="1">liuqiaochu0205</a></cite>
<em><span>2011-5-18 15:35</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=913752&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">71</a><em>65699</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-YvettePanHKU.html" c="1">YvettePanHKU</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=913752&goto=lastpost#lastpost">2021-4-30 08:30</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2078246">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2078246&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2078246&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >抽到重测ot的同学们收到par面情况</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-8504088.html" c="1">cynthia0926</a></cite>
<em><span>2016-11-27 17:12</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2078246&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">9</a><em>22979</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Bigggbeauty.html" c="1">Bigggbeauty</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2078246&goto=lastpost#lastpost">2021-4-30 08:28</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2318970">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318970&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318970&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" style="color: #8F2A90;" onclick="atarget(this)" class="xst" >HK所 FRM面试</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10720601.html" c="1">instantpig</a></cite>
<em><span>2021-4-6 14:01</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318970&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>1139</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-instantpig.html" c="1">instantpig</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2318970&goto=lastpost#lastpost">2021-4-29 20:30</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2297215">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2297215&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2297215&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >统计：毕马威SZ所秋招审计收到面试情况</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13101053.html" c="1">_**_jw</a></cite>
<em><span>2020-11-1 22:01</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2297215&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>1161</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%CC%EC%C6%BDstory.html" c="1">天平story</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2297215&goto=lastpost#lastpost">2021-4-29 10:01</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319353">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319353&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319353&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >西安所审计m+par面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13702159.html" c="1">YZY775</a></cite>
<em><span>2021-4-16 09:40</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319353&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">3</a><em>505</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%D5%D2%B8%F6%BA%C3%B9%A4%D7%F7%B0%A1%B0%A1%B0%A1.html" c="1">找个好工作啊啊啊</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319353&goto=lastpost#lastpost">2021-4-28 18:00</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321525">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321525&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321525&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG HK所 Auidt</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13134064.html" c="1">eeezzz</a></cite>
<em><span>2021-4-28 17:33</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321525&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>104</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-eeezzz.html" c="1">eeezzz</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321525&goto=lastpost#lastpost">2021-4-28 17:33</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321426">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321426&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321426&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >SZ 审计 春招</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13340881.html" c="1">岛田一颗糖</a></cite>
<em><span>2021-4-27 21:27</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321426&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>258</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Makyo2019.html" c="1">Makyo2019</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321426&goto=lastpost#lastpost">2021-4-28 14:25</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320826">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320826&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320826&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG春招BJ</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12530434.html" c="1">candy123456hahhahhah</a></cite>
<em><span>2021-4-22 14:01</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320826&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">15</a><em>2066</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-candy123456hahhahhah.html" c="1">candy123456hahhahhah</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320826&goto=lastpost#lastpost">2021-4-28 10:15</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321185">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321185&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321185&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KPMG暑期实习群面面经</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13537440.html" c="1">youngbin6</a></cite>
<em><span>2021-4-25 23:17</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321185&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">3</a><em>291</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-jiacli19.html" c="1">jiacli19</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321185&goto=lastpost#lastpost">2021-4-27 13:11</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2303032">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2303032&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2303032&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >HZ KPMG PAR面时间</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-11437848.html" c="1">大圣313</a></cite>
<em><span>2020-11-17 10:07</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2303032&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">4</a><em>1000</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B4%F3%CA%A5313.html" c="1">大圣313</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2303032&goto=lastpost#lastpost">2021-4-27 12:15</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2321343">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321343&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321343&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >毕马威收到offer</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12626432.html" c="1">tongtong12345678</a></cite>
<em><span>2021-4-27 12:08</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2321343&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">0</a><em>397</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-tongtong12345678.html" c="1">tongtong12345678</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2321343&goto=lastpost#lastpost">2021-4-27 12:08</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2304505">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2304505&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2304505&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >BJ所11.12管理咨询-财务管理咨询MC-FC业务线M面后进度调查</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12561731.html" c="1">WoodyHu</a></cite>
<em><span>2020-11-20 16:55</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2304505&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>449</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-luckyiiiiii.html" c="1">luckyiiiiii</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2304505&goto=lastpost#lastpost">2021-4-26 15:41</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2317643">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317643&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="投票 - 有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/pollsmall.gif" alt="投票" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317643&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >北京  风险咨询  日常实习生 M面之后多久Par面</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13666214.html" c="1">一颗哒哒哒菠萝</a></cite>
<em><span>2021-3-19 22:47</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317643&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">15</a><em>508</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-Wowoo1126.html" c="1">Wowoo1126</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2317643&goto=lastpost#lastpost">2021-4-26 10:51</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2320304">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320304&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320304&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >2021春招新鲜面经</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13783357.html" c="1">jisoo666</a></cite>
<em><span>2021-4-18 16:08</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2320304&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">8</a><em>1532</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B6%DF%C0%B2A%C3%CE%B5%C4%D0%A1%BF%DA%B4%FC%C4%D8.html" c="1">哆啦A梦的小口袋呢</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2320304&goto=lastpost#lastpost">2021-4-26 01:06</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2318250">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318250&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318250&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >KP superday SZ</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/common/digest_1.gif" align="absmiddle" alt="digest" title="精华 1" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12338618.html" c="1">Icebell</a></cite>
<em><span>2021-3-27 15:12</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2318250&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">5</a><em>987</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%B6%DF%C0%B2A%C3%CE%B5%C4%D0%A1%BF%DA%B4%FC%C4%D8.html" c="1">哆啦A梦的小口袋呢</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2318250&goto=lastpost#lastpost">2021-4-26 00:48</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2317795">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317795&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317795&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >一起组队mock吧</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13778760.html" c="1">BYH2021</a></cite>
<em><span>2021-3-22 19:31</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2317795&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">9</a><em>395</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-youngbin6.html" c="1">youngbin6</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2317795&goto=lastpost#lastpost">2021-4-25 23:23</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319569">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319569&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319569&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >有组队模拟群面case的吗？</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-12383518.html" c="1">蜗牛56</a></cite>
<em><span>2021-4-12 12:06</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319569&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">1</a><em>217</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-youngbin6.html" c="1">youngbin6</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319569&goto=lastpost#lastpost">2021-4-25 23:19</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319651">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319651&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319651&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >关于BJ所manager面问题</a>
<img src="https://bbsimg.yingjiesheng.net/static/image/stamp/011.small.gif" alt="新人帖" align="absmiddle" />
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-13583963.html" c="1">helen_l</a></cite>
<em><span>2021-4-12 23:07</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319651&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">7</a><em>1028</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-hqq77.html" c="1">hqq77</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319651&goto=lastpost#lastpost">2021-4-25 23:14</a></em>
</td>
</tr>
</tbody>
<tbody id="normalthread_2319042">
<tr>
<td class="icn">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319042&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" title="有新回复 - 新窗口打开" target="_blank">
<img src="https://bbsimg.yingjiesheng.net/static/image/common/folder_new.gif" />
</a>
</td>
<th class="new">
<em>[<a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&amp;filter=typeid&amp;typeid=594">面试</a>]</em> <a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319042&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" onclick="atarget(this)" class="xst" >bj审计春招</a>
</th>
<td class="by">
<cite>
<a href="https://bbs.yingjiesheng.com/space-uid-10836498.html" c="1">李冉5</a></cite>
<em><span>2021-4-6 21:52</span></em>
</td>
<td class="num"><a href="https://bbs.yingjiesheng.com/forum.php?mod=viewthread&amp;tid=2319042&amp;extra=page%3D1%26filter%3Dtypeid%26typeid%3D594%26orderby%3Ddateline%250A" class="xi2">2</a><em>517</em></td>
<td class="by">
<cite><a href="https://bbs.yingjiesheng.com/space-username-%BA%AB%D0%A1%C5%D6%D1%BD.html" c="1">韩小胖呀</a></cite>
<em><a href="https://bbs.yingjiesheng.com/forum.php?mod=redirect&tid=2319042&goto=lastpost#lastpost">2021-4-25 02:29</a></em>
</td>
</tr>
</tbody>
</table>
</form>
</div>
</div>

<div id="filter_special_menu" class="p_pop" style="display:none" change="location.href='forum.php?mod=forumdisplay&fid=456&filter='+$('filter_special').value">
<ul>
<li><a href="https://bbs.yingjiesheng.com/forum-456-1.html">全部主题</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=specialtype&amp;specialtype=poll&typeid=594&orderby=dateline%0A">投票</a></li><li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=specialtype&amp;specialtype=reward&typeid=594&orderby=dateline%0A">悬赏</a></li><li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=specialtype&amp;specialtype=activity&typeid=594&orderby=dateline%0A">活动</a></li><li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=specialtype&amp;specialtype=debate&typeid=594&orderby=dateline%0A">辩论</a></li></ul>
</div>
<div id="filter_dateline_menu" class="p_pop" style="display:none">
<ul>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&typeid=594&orderby=dateline%0A">时间</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=86400&typeid=594&orderby=dateline%0A">一天</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=172800&typeid=594&orderby=dateline%0A">两天</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=604800&typeid=594&orderby=dateline%0A">一周</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=2592000&typeid=594&orderby=dateline%0A">一个月</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;orderby=lastpost&amp;filter=dateline&amp;dateline=7948800&typeid=594&orderby=dateline%0A">三个月</a></li>
</ul>
</div>
<div id="filter_orderby_menu" class="p_pop" style="display:none">
<ul>
<li><a href="https://bbs.yingjiesheng.com/forum-456-1.html">默认排序</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=author&amp;orderby=dateline&typeid=594">发帖时间</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=reply&amp;orderby=replies&typeid=594">回复/查看</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=reply&amp;orderby=views&typeid=594">查看</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=lastpost&amp;orderby=lastpost&typeid=594">最后发表</a></li>
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&amp;fid=456&amp;filter=heat&amp;orderby=heats">热门</a></li>
<ul>
</div>

<div class="bm bw0 pgs cl">
<span id="fd_page_bottom"><div class="pg"><strong>1</strong><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=2">2</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=3">3</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=4">4</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=5">5</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=6">6</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=7">7</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=8">8</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=9">9</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=10">10</a><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=155" class="last">... 155</a><label><input type="text" name="custompage" class="px" size="2" title="输入页码，按回车快速跳转" value="1" onkeydown="if(event.keyCode==13) {window.location='forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page='+this.value;; doane(event);}" /><span title="共 155 页"> / 155 页</span></label><a href="https://bbs.yingjiesheng.com/forum.php?mod=forumdisplay&fid=456&typeid=594&orderby=dateline%0A&filter=typeid&typeid=594&orderby=dateline%0A&amp;page=2" class="nxt">下一页</a></div></span>
<span  class="pgb y"><a href="https://bbs.yingjiesheng.com/forum.php">返&nbsp;回</a></span>
<a href="javascript:;" id="newspecialtmp" onmouseover="$('newspecial').id = 'newspecialtmp';this.id = 'newspecial';showMenu({'ctrlid':this.id})" onclick="showWindow('newthread', 'forum.php?mod=post&action=newthread&fid=456')" title="发新帖"><img src="https://bbsimg.yingjiesheng.net/static/image/common/pn_post.png" alt="发新帖" /></a></div>
<!--[diy=diyfastposttop]--><div id="diyfastposttop" class="area"></div><!--[/diy]-->
<script type="text/javascript">
var postminchars = parseInt('4');
var postmaxchars = parseInt('2000000');
var disablepostctrl = parseInt('0');
var fid = parseInt('456');
</script>
<div id="f_pst" class="bm">
<div class="bm_h">
<h2>快速发帖</h2>
</div>
<div class="bm_c">
<form method="post" autocomplete="off" id="fastpostform" action="forum.php?mod=post&amp;action=newthread&amp;fid=456&amp;topicsubmit=yes&amp;infloat=yes&amp;handlekey=fastnewpost" onSubmit="return fastpostvalidate(this)">

<div id="fastpostreturn" style="margin:-5px 0 5px"></div>

<div class="pbt cl">
<div class="ftid">
<select name="typeid" id="typeid_fast" width="80">
<option value="0" selected="selected">选择主题分类</option><option value="591">问答</option>
<option value="592">其他</option>
<option value="593">笔试</option>
<option value="594">面试</option>
<option value="595">网申</option>
<option value="596">公司概况</option>
<option value="597">综合经验</option>
<option value="598">签约</option>
</select>
</div>
<script type="text/javascript" reload="1">simulateSelect('typeid_fast');</script>
<input type="text" id="subject" name="subject" class="px" value="" onkeyup="strLenCalc(this, 'checklen', 80);" tabindex="11" style="width: 25em" />
<span>还可输入 <strong id="checklen">80</strong> 个字符</span>
</div>

<div class="cl">
<div id="fastsmiliesdiv" class="y"><div id="fastsmiliesdiv_data"><div id="fastsmilies"></div></div></div><div class="hasfsl" id="fastposteditor">
<div class="tedt">
<div class="bar">
<span class="y">
<a href="https://bbs.yingjiesheng.com/forum.php?mod=post&amp;action=newthread&amp;fid=456" onclick="switchAdvanceMode(this.href);doane(event);">高级模式</a>
</span><script src="static/js/seditor.js?jN8" type="text/javascript"></script>
<div class="fpd">
<a href="javascript:;" title="文字加粗" class="fbld" onclick="seditor_insertunit('fastpost', '[b]', '[/b]');doane(event);">B</a>
<a href="javascript:;" title="设置文字颜色" class="fclr" id="fastpostforecolor" onclick="showColorBox(this.id, 2, 'fastpost');doane(event);">Color</a>
<a id="fastpostimg" href="javascript:;" title="图片" class="fmg" onclick="seditor_menu('fastpost', 'img');doane(event);">Image</a>
<a id="fastposturl" href="javascript:;" title="添加链接" class="flnk" onclick="seditor_menu('fastpost', 'url');doane(event);">Link</a>
<a id="fastpostquote" href="javascript:;" title="引用" class="fqt" onclick="seditor_menu('fastpost', 'quote');doane(event);">Quote</a>
<a id="fastpostcode" href="javascript:;" title="代码" class="fcd" onclick="seditor_menu('fastpost', 'code');doane(event);">Code</a>
<a href="javascript:;" class="fsml" id="fastpostsml" onclick="showMenu({'ctrlid':this.id,'evt':'click','layer':2});return false;">Smilies</a>
<script type="text/javascript" reload="1">smilies_show('fastpostsmiliesdiv', 8, 'fastpost');</script>
<span class="pipe z">|</span><span id="spanButtonPlaceholder">上传</span></div></div>
<div class="area">
<textarea rows="6" cols="80" name="message" id="fastpostmessage" onKeyDown="seditor_ctlent(event, '$(\'fastpostsubmit\').click()');" tabindex="12" class="pt"></textarea>
</div>
</div>
</div>
<div id="seccheck_fastpost">
<div class="mtm"><span id="secqaa_qSTCr0qz"></span>		
<script type="text/javascript" reload="1">updatesecqaa('qSTCr0qz', '<sec> <span id="sec<hash>" onclick="showMenu(this.id)"><sec></span><div id="sec<hash>_menu" class="p_pop p_opt" style="display:none"><sec></div>', 'forum::forumdisplay');</script>
</div></div>

<input type="hidden" name="formhash" value="34ccfd75" />
<input type="hidden" name="usesig" value="" />
</div>

<script type="text/javascript">
var editorid = '';
var ATTACHNUM = {'imageused':0,'imageunused':0,'attachused':0,'attachunused':0}, ATTACHUNUSEDAID = new Array(), IMGUNUSEDAID = new Array();
</script>

<input type="hidden" name="posttime" id="posttime" value="1620878151" />
<div class="upfl hasfsl">
<table cellpadding="0" cellspacing="0" border="0" width="100%" id="attach_tblheader" style="display: none">
<tr>
<td>点击附件文件名添加到帖子内容中</td>
<td class="atds">描述</td>
<td class="attc"></td>
</tr>
</table>
<div class="fieldset flash" id="attachlist"></div>
<script src="static/js/upload.js?jN8" type="text/javascript"></script><script type="text/javascript">
var upload = new SWFUpload({
upload_url: "https://bbs.yingjiesheng.com/misc.php?mod=swfupload&action=swfupload&operation=upload&fid=456",
post_params: {"uid" : "13906980", "hash":"643a32396609024d17203dc3b03d3cf0"},
file_size_limit : "2976",
file_types : "*.gif;*.jpg;*.jpeg;*.png;*.doc;*.docx;*.xls;*.xlsx;*.pdf;*.txt;*.ppt",
file_types_description : "All Support Formats",
file_upload_limit : 20,
file_queue_limit : 0,
swfupload_preload_handler : preLoad,
swfupload_load_failed_handler : loadFailed,
file_dialog_start_handler : fileDialogStart,
file_queued_handler : fileQueued,
file_queue_error_handler : fileQueueError,
file_dialog_complete_handler : fileDialogComplete,
upload_start_handler : uploadStart,
upload_progress_handler : uploadProgress,
upload_error_handler : uploadError,
upload_success_handler : uploadSuccess,
upload_complete_handler : uploadComplete,
button_image_url : "https://bbsimg.yingjiesheng.net/static/image/common/uploadbutton_small.png",
button_placeholder_id : "spanButtonPlaceholder",
button_width: 17,
button_height: 25,
button_cursor:SWFUpload.CURSOR.HAND,
button_window_mode: "transparent",
custom_settings : {
progressTarget : "attachlist",
uploadSource: 'forum',
uploadType: 'attach',
maxAttachNum: 20,
uploadFrom: 'fastpost'
},
debug: false
});
</script>
</div>

<p class="ptm pnpost">
<a href="https://bbs.yingjiesheng.com/home.php?mod=spacecp&amp;ac=credit&amp;op=rule&amp;fid=456" class="y" target="_blank">本版积分规则</a>
<button type="submit" name="topicsubmit" id="fastpostsubmit" value="topicsubmit" tabindex="13" class="pn pnc"><strong>发表帖子</strong></button>
</p>
</form>
</div>
</div>
<!--[diy=diyforumdisplaybottom]--><div id="diyforumdisplaybottom" class="area"></div><!--[/diy]-->
</div>

</div>
</div>
<ul class="p_pop" id="newspecial_menu" style="display: none">
<li><a href="https://bbs.yingjiesheng.com/forum.php?mod=post&amp;action=newthread&amp;fid=456">发表帖子</a></li><li class="poll"><a href="https://bbs.yingjiesheng.com/forum.php?mod=post&amp;action=newthread&amp;fid=456&amp;special=1">发起投票</a></li><li class="reward"><a href="https://bbs.yingjiesheng.com/forum.php?mod=post&amp;action=newthread&amp;fid=456&amp;special=3">发布悬赏</a></li><li class="debate"><a href="https://bbs.yingjiesheng.com/forum.php?mod=post&amp;action=newthread&amp;fid=456&amp;special=5">发起辩论</a></li></ul>
<script type="text/javascript">document.onkeyup = function(e){keyPageScroll(e, 0, 1, 'forum.php?mod=forumdisplay&fid=456&filter=typeid&orderby=lastpost&typeid=594&orderby=dateline%0A&', 1);}</script>

<div class="wp mtn">
<!--[diy=diy3]--><div id="diy3" class="area"></div><!--[/diy]-->
</div>	</div>
<div class="focus" id="sitefocus">
<div class="bm">
<div class="bm_h cl">
<a href="javascript:;" onclick="setcookie('nofocus_forum', 1, 1*3600);$('sitefocus').style.display='none'" class="y" title="关闭">关闭</a>
<h2>
站长推荐<span id="focus_ctrl" class="fctrl"><img src="https://bbsimg.yingjiesheng.net/static/image/common/pic_nv_prev.gif" alt="上一条" title="上一条" id="focusprev" class="cur1" onclick="showfocus('prev');" /> <em><span id="focuscur"></span>/1</em> <img src="https://bbsimg.yingjiesheng.net/static/image/common/pic_nv_next.gif" alt="下一条" title="下一条" id="focusnext" class="cur1" onclick="showfocus('next')" /></span>
</h2>
</div>
<div class="bm_c" id="focus_con">
</div>
</div>
</div><div class="bm_c" style="display: none" id="focus_0">
<dl class="xld cl bbda">
<dt><a href="http://bbs.yingjiesheng.com/thread-350390-1-1.html" class="xi2" target="_blank"><a href="/thread-350390-1-1.html" target=_blank>应届生BBS每日精彩主题推荐</a></a></dt>
<dd><a href="/thread-350390-1-1.html" target=_blank>应届生BBS每日精彩主题推荐，点击查看</a></dd>
</dl>
<p class="ptn cl"><a href="http://bbs.yingjiesheng.com/thread-350390-1-1.html" class="xi2 y" target="_blank">查看 &raquo;</a></p>
</div><script type="text/javascript">
var focusnum = 1;
if(focusnum < 2) {
$('focus_ctrl').style.display = 'none';
}
if(!$('focuscur').innerHTML) {
var randomnum = parseInt(Math.round(Math.random() * focusnum));
$('focuscur').innerHTML = Math.max(1, randomnum);
}
showfocus();
var focusautoshow = window.setInterval('showfocus(\'next\', 1);', 5000);
</script>


<script type="text/javascript">var cookieLogin = Ajax("TEXT");cookieLogin.get("connect.php?mod=check&op=cookie", function() {});</script>

<script type="text/javascript">showWindow("freeaddon_daily_topic","plugin.php?id=freeaddon_daily_topic", "get", 0);</script>

<div id="ft" class="wp cl">
<div id="flk" class="y">
<p><a href="http://vip.yingjiesheng.com/app/" target="_blank"  style="color: red">应届生APP</a><span class="pipe">|</span><a href="javascript:;"  onclick="showWindow('miscreport', 'misc.php?mod=report&url='+REPORTURL);return false;">举报</a><span class="pipe">|</span><a href="http://bbs.yingjiesheng.com/archiver/" >Archiver</a><span class="pipe">|</span><strong><a href="https://bbs.yingjiesheng.com" target="_blank">应届生求职网YingJieSheng.COM</a></strong>
( <a href="http://www.miitbeian.gov.cn/" target="_blank">沪ICP备12015550号-13</a> )<span style="display: none;">
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fb15730ce74e116ff0df97e207706fa4a' type='text/javascript'%3E%3C/script%3E"));
</script>
</span></p>
<p class="xs0">
GMT+8, 2021-5-13 11:55<span id="debuginfo">
</span>
</p>
</div>
<div id="frt">
<p>Powered by <strong><a href="http://www.discuz.net" target="_blank">Discuz!</a></strong> <em>X3.2</em></p>
<p class="xs0">&copy; 2001-2012 <a href="http://www.comsenz.com" target="_blank">Comsenz Inc.</a></p>

<p style="background-color:#fff;text-align: center;">
        <a href="http://sh.cyberpolice.cn/infoCategoryListAction.do?act=initjpg"><img src="//static1.yingjiesheng.net/html/images/police.gif" /></a>&nbsp;&nbsp;
        <a href="http://www.zx110.org/"><img src="//static1.yingjiesheng.net/html/images/wlsh.gif" /></a>&nbsp;&nbsp;
        <a href="https://www.sgs.gov.cn/lz/licenseLink.do?method=licenceView&amp;entyId=dov73ne26zbqppw8cklwn9rl7z1dwyd3pz" target="_blank"><img src="//static1.yingjiesheng.net/html/images/shgs.gif" /></a>&nbsp;&nbsp;
        <script src="//kxlogo.knet.cn/seallogo.dll?sn=e13112711010043621l7jl000000&size=0" type="text/javascript"></script>&nbsp;&nbsp;
        <a href="http://report.12377.cn:13225/toreportinputNormal_anis.do" target="_blank"><img src="//static1.yingjiesheng.net/html/images/shjubao2.gif" /></a>
    </p>
</div><script type="text/javascript">
var invisiblestatus = '在线';
var loginstatusobj = $('loginstatusid');
if(loginstatusobj != undefined && loginstatusobj != null) loginstatusobj.innerHTML = invisiblestatus;
</script>
</div>

<div id="g_upmine_menu" class="tip tip_3" style="display:none;">
<div class="tip_c">
积分 46, 距离下一级还需 74 积分
</div>
<div class="tip_horn"></div>
</div>
<div id="scrolltop">
<span hidefocus="true"><a title="返回顶部" onclick="window.scrollTo('0','0')" class="scrolltopa" ><b>返回顶部</b></a></span>
<span>
<a href="https://bbs.yingjiesheng.com/forum.php" hidefocus="true" class="returnboard" title="返回版块"><b>返回版块</b></a>
</span>
</div>
<script type="text/javascript">_attachEvent(window, 'scroll', function () { showTopLink(); });checkBlind();</script>
			<div id="discuz_tips" style="display:none;"></div>
			<script type="text/javascript">
				var tipsinfo = '3353725|X3.2|0.6||0||13906980|11|1620878151|a8562a510dada178424ffb5846fda746|2';
			</script></body>
</html>"""
discuss_posts = soup.find_all(class_='xst')
soup.find_pa()
# print('discuss_posts', discuss_posts)
for discuss_post in discuss_posts:
    discuss_post
    # print(discuss_post)
    # try:
    #     title = discuss_post.string
    #     # url = discuss_post['href']
    #     url = discuss_post.get('href')
    # except:
    #     continue