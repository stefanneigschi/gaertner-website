const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1200,height:1400},deviceScaleFactor:2});
await p.goto('file:///home/user/gaertner-website/social/html/feed.html');await p.waitForTimeout(800);
await p.screenshot({path:'/home/user/gaertner-website/social/feed-mockup.png'});await b.close();})();
