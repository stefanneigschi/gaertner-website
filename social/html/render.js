const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{const R='/home/user/gaertner-website/social';
const list=JSON.parse(fs.readFileSync(R+'/html/list.json'));
const b=await chromium.launch({args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
for(const n of list){await p.goto('file://'+R+'/html/'+n+'.html');await p.waitForTimeout(400);
 const ov=await p.evaluate(()=>{const post=document.querySelector('.p');return post.scrollHeight-post.clientHeight});
 await p.screenshot({path:R+'/posts/'+n+'.png'});console.log(n,'overflow',ov);}
await b.close();})();
