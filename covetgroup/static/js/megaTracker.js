function getUrl(){var e=localStorage.getItem("PageTrackConv"),t=JSON.parse(e);t=t[Object.keys(JSON.parse(e)).sort().pop()];var r=t[0].url,a=t[1].url;return data={referrer:r,url_origin:a,flow:e}}function delUrl(){var e=localStorage.getItem("PageTrackConv"),t=JSON.parse(e);t=t[Object.keys(JSON.parse(e)).sort().pop()],localStorage.removeItem("PageTrackConv");var r={};r[0]=t,localStorage.setItem("PageTrackConv",JSON.stringify(r))}var session={},page=[],referer,time=(new Date).toLocaleString(),date_diff_indays=function(e,t){return dt1=new Date(e),dt2=new Date(t),Math.floor((Date.UTC(dt2.getFullYear(),dt2.getMonth(),dt2.getDate())-Date.UTC(dt1.getFullYear(),dt1.getMonth(),dt1.getDate()))/864e5)};null===localStorage.getItem("PageTrackConv")?(referer=document.referrer,referer||(referer="(direct)"),page.push({url:referer,date:time}),page.push({url:window.location.href,date:time}),session[0]=page,page=null):(session=JSON.parse(localStorage.getItem("PageTrackConv")),date_diff_indays(session[Object.keys(session).length-1][session[Object.keys(session).length-1].length-1].date,time)>=1&&(referer=document.referrer,referer||(referer="(direct)"),page.push({url:referer,date:time}),page.push({url:window.location.href,date:time}),session[Object.keys(session).length]=page),session[Object.keys(session).length-1][session[Object.keys(session).length-1].length-1].url!=window.location.href?session[Object.keys(session).length-1].push({url:window.location.href,date:time}):null,page=null),localStorage.setItem("PageTrackConv",JSON.stringify(session));