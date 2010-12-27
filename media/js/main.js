(function($){
    /*
     * post = {'avatar':'bla.jpg','content':'bla..bla..','datetime':'20 Nov 87'}
     */
    $.prepend_post = function(post){
        $('#posts').prepend($('<div></div>').addClass('post')
            .append($('<img/>').attr('src',post.avatar))
            .append($('<span></span>').addClass('content').html(post.content))
            .append($('<span></span>').addClass('datetime').html(post.datetime)));
    };
    
    $.append_post = function(post){
        $('#posts').append($('<div></div>').addClass('post')
            .append($('<img/>').attr('src',post.avatar))
            .append($('<span></span>').addClass('content').html(post.content))
            .append($('<span></span>').addClass('datetime').html(post.datetime)));
    };
    
    $.since_id = 0;
    $.max_id = 0;
    $.post_waiting = [];
    
    $.firstload = function(){
        $('#more').html('LOADING....');
        $.ajax({
            url: '/newsfeed/firstload',
            dataType: 'json',
            success: function(posts) {
                $.max_id = posts[posts.length - 1].id;
                $.since_id = posts[0].id;
                $.each(posts, function(index, post){
                    $.append_post(post);
                    $('#more').html('MORE');
                });
            },
        });
    };
    
    $.more = function(){
        $('#more').html('LOADING....');
        $.ajax({
            url: '/newsfeed/older/' + $.since_id,
            dataType: 'json',
            success: function(posts) {
                $.since_id = posts[posts.length - 1].id;
                $.each(posts, function(index, post){
                    $.append_post(post);
                    $('#more').html('MORE');
                });
            },
        });
        
    };
    
    $.newest = function(){
        $.ajax({
            url: '/newsfeed/newest/' + $.max_id,
            dataType: 'json',
            success: function(posts) {
                $.post_waiting = posts;
                if($.post_waiting.length > 0) {
                    $('#newest').html($.post_waiting.length + ' NEW POST').fadeIn();
                }
            },
        });
        
    };
    
    
    
    $(document).ready(function(){
        $('#more').click($.more);
        $.firstload();
    })
})(jQuery)
