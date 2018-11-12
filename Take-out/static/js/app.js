(function(win) {
        var docEl = win.document.documentElement;
        var time;

        function refreshRem() {
                var width = docEl.clientWidth;
                if (width > 768) { // 最大宽度
                        width = 768;
                }
                var rem = width / 10; // 将屏幕宽度分成10份， 1份为1rem
                docEl.style.fontSize = rem + 'px';
                //把rem的值给根元素的font-size
                ///rem用font-size:75px来进行换算
                // 40/75
                // 20/37.5
        }

        win.addEventListener('resize', function() {
                clearTimeout(time);
                time = setTimeout(refreshRem, 1);
        }, false);
        win.addEventListener('pageshow', function(e) {
                if (e.persisted) {
                        clearTimeout(time);
                        time = setTimeout(refreshRem, 1);
                }
        }, false);

        refreshRem();

})(window);

//onpageshow 事件类似于 onload 事件，onload 事件在页面第一次加载时触发， onpageshow 事件在每次加载页面时触发，即 onload 事件在页面从浏览器缓存中读取时不触发。
//为了查看页面是直接从服务器上载入还是从缓存中读取，可以使用 PageTransitionEvent 对象的 persisted 属性来判断。 如果页面从浏览器的缓存中读取该属性返回 true，否则返回 false