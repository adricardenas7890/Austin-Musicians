// Create a function to highlight the active page on the nav bar
$(function()
{
    // For each "a" tag (aka any link)
    $('a').each(function(){
        //  If the link has a page it points to and it has the nav-link class
        if (($(this).prop('href') == window.location.href) && ($(this).hasClass('nav-link')))
        {
            // Add active class
            $(this).addClass('active');
        }
    });
});