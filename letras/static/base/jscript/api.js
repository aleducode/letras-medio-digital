(function($) {
  $.fn.SocialCounter = function(options) {
    var settings = $.extend({
      // These are the defaults.
      twitter_user:'',
      facebook_user:'',
      facebook_token:'',
      instagram_user:'',
      instagram_user_sandbox:'',
      instagram_token:'',
      google_plus_id:'',
      google_plus_key:'',
      linkedin_oauth:'',
      youtube_user:'',
      youtube_user_square:'',
      youtube_key:'',
      vine_user:'',
      pinterest_user:'',
      dribbble_user:'',
      dribbble_token:'',
      soundcloud_user_id:'',
      soundcloud_client_id:'',
      vimeo_user:'',
      vimeo_token:'',
      github_user:'',
      behance_user:'',
      behance_client_id:'',
      vk_id:'',
      foursquare_user:'',
      foursquare_token:'',
      tumblr_username:'',
      twitch_username:'',
      twitch_client_id:'',
      spotify_artist_id:'',
      spotify_user_id:''
    }, options);

    function facebook(){
      //Facebook API
      //60 Day Access Token - Regenerate a new one after two months
      //https://neosmart-stream.de/facebook/how-to-create-a-facebook-access-token/
      //https://smashballoon.com/custom-facebook-feed/access-token/
      $.ajax({
        url: 'https://graph.facebook.com/v3.2/'+settings.facebook_user+'?fields=fan_count',
        dataType: 'json',
        type: 'GET',
        data: {
          access_token:settings.facebook_token,
        },
        success: function(data) {
          var followers = parseInt(data.fan_count);
          var k = kFormatter(followers);
          $('#wrapper .item.facebook .count').append(k); 
          $('#wrapper .item.facebook').attr('href','https://facebook.com/'+settings.facebook_user);
          getTotal(followers); 
        } 
      }); 
    }
    https://graph.facebook.com/v3.2/alejoduquecorrea?access_token=EAAENSQQ4k6YBALZC2fkZBANDseyGyEktfgAJyccCOvF1luPTCuIEa31nnll58ADZCdjofPNtmLZA4PdiZBmF0w57v65xfbIly7d6bdaeRLNZCMacbdueqxl4Q4pdewTRbw3mqCZB8Ka1YyUzovHJ5W3x1lbeZCLPZCufA7MZBqdrcDdt5KVLzLvUdjCTfZBVC55yicrl8HZAR7zd1Offaamve0SHP5Gbt7cPRw4ZD&fields=friends
    function instagram(){
      $.ajax({
        url: 'https://api.instagram.com/v1/users/self/',
        dataType: 'jsonp',
        type: 'GET',
        data: {
          access_token: settings.instagram_token
        },
        success: function(data) {
          var followers = parseInt(data.data.counts.followed_by);
          var k = kFormatter(followers);
          $('#wrapper .item.instagram .count').append(k);
          $('#wrapper .item.instagram').attr('href','https://instagram.com/'+settings.instagram_user);
          getTotal(followers); 
        }
      });
    }
    function instagram_sandbox(){
       $.ajax({
         url: 'https://api.instagram.com/v1/users/search?q='+settings.instagram_user_sandbox,
         dataType: 'jsonp',
         type: 'GET',
         data: {
           access_token: settings.instagram_token
         },
         success: function(data) {
           $.each(data.data, function(i, item) {
             if(settings.instagram_user_sandbox == item.username){
               $.ajax({
                 url: "https://api.instagram.com/v1/users/" + item.id,
                 dataType: 'jsonp',          
                 type: 'GET',
                 data: {
                   access_token: settings.instagram_token
                 },
                 success: function(data) {
                   var followers = parseInt(data.data.counts.followed_by);
                   var k = kFormatter(followers);
                   $('#wrapper .instagram_sandbox .count').append(k);
                   $('#wrapper .item.instagram_sandbox').attr('href','https://instagram.com/'+settings.instagram_user_sandbox);
                   getTotal(followers); 
                 }
               });
             } 
           });
         }
       });
     }
   

    // function twitter(){
    //   $.ajax({
    //     url: '../SocialCounters/twitter/index.php',
    //     dataType: 'json',
    //     type: 'GET',
    //     data:{
    //       user:settings.twitter_user
    //     },
    //     success: function(data) {   
    //       var followers = parseInt(data.followers);
    //       $('#wrapper .item.twitter .count').append(followers).digits(); 
    //       $('#wrapper .item.twitter').attr('href','https://twitter.com/'+settings.twitter_user);
    //       getTotal(followers); 
    //     } 
    //   }); 
    // }

    //Function to add commas to the thousandths
    $.fn.digits = function(){ 
      return this.each(function(){ 
        $(this).text( $(this).text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") ); 
      })
    }
    //Function to add K to thousands
    function kFormatter(num) {
      return num > 999 ? (num/1000).toFixed(1) + 'k' : num;
    }
    //Function to add K to thousands
    function mFormatter(num) {
      return num > 999999 ? (num/1000000).toFixed(1) + 'm' : num;
    }
    //Total Counter
    var total = 0;
    //Get an integer paramenter from each ajax call
    function getTotal(data) {
      total = total + data;
      $("#total").html(total).digits();
      $("#total_k").html(kFormatter(total));
    }

    function linkClick(){
      $('#wrapper .item').attr('target','_blank');
    }
    linkClick();

    //Call Functions
    // if(settings.twitter_user!=''){ 
    //   twitter(); 
    //} 
    if(settings.facebook_user!='' && settings.facebook_token!=''){ 
      facebook(); 
    } if(settings.instagram_user!='' && settings.instagram_token!=''){ 
      instagram();
    } 
  };
}(jQuery));
