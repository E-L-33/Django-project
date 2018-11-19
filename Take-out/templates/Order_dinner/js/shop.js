function isInt(str) {
  return  /^[-\+]?\d+$/.test($.trim(str));
}
function calcprice(){
  var total=0;
  var totalprice=0;
  $('.cart_good').each(function(){
    var $this=$(this);
    var sel=$this.attr('sel')=='1';
    if(sel){
      var num=$this.find('.shownum').val();
      if(isNaN(num)){
        num=1;
      }
      $this.find('.shownum').val(num);
      total+=parseInt(num);
      totalprice+=parseFloat($this.find('.shownum').val())*parseFloat($this.data('marketprice'));
    }
  });
  $('.total').html(total);
  $('.totalprice').html(totalprice.toFixed(2));  //toFixed() 方法可把 Number 四舍五入为指定小数位数的数字。
  return total;
}
require(['tpl', 'core'], function(tpl, core) {
   //数量减法
   $('.leftnav').click(function(){
      var input=$(this).next();
      if(!isInt(input.val())){   //isint方法来判断文本框中读入的是不是数字
        input.val('1');
      }
      var num=parseInt(input.val());
      num--;
      if(num <=0){
        num=1;
      }
      input.val(num);
      //ajaxpost到服务端
      //http://upin.chenhua.cc/app/index.php?i=4&c=entry&do=shop&m=ewei_shop&p=cart&op=updatenum&id=12&goodsid=4&total=3
      //core.json('shop/cart',{'op':'updatenum',id:$(this).closest('.cart_good').data('cartid'),goodsid:$(this).closest('.cart_good').data('goodsid'), total:num},null,false,true);
      calcprice();
   })
   //数量增加
   $('.rightnav').click(function(){
     var maxbuy=parseInt($(this).closest('.cart_good').data('maxbuy'));
     var stock=parseInt($(this).closest('.cart_good').data('stock'));
     var input=$(this).prev();
     if(!isInt(input.val())){
       input.val(1);
     }
     var num=parseInt(input.val());
     num++;
     if(num > maxbuy && maxbuy > 0){
      num=maxbuy;
      alert('您最多购买'+maxbuy+'件');
     }else if(stock !='-1' && stock !='' && num > stock){
      num=stock;
      alert('您最多购买'+stock+'件');
     }
     input.val(num);
    // core.json('shop/cart',{'op':'updatenum',id:$(this).closest('.cart_good').data('cartid'),goodsid:$(this).closest('.cart_good').data('goodsid'), total:num},null,false,true);
     calcprice();
   })
})