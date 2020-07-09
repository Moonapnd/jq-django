console.log('ssssssssssssss')
$(document).ready(function(){
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val()
    $('#create-mail-btn').click(function(){
        var serializedData = $('#mail-form').serialize();
        $.ajax({
            url: $('#mail-form').data('url'),
            data: serializedData,
            type: 'post',
            success: function(response){
                $('#mail-list').append("<div class='card card-body mb-2' id='mail-item' data-id='" + response.mail.id  +"'>" + response.mail.title + "<button type='button' class='close float-right'><span aria-hiden='true'>&times;</span></button></div>")
            }
        })
        $('#mail-form')[0].reset(); // clear form after submit
    })

    $('#mail-list').on('click', '.card', function(){
        var dataId = $(this).data('id');
        $.ajax({
            url: '/mail_list/' + dataId + '/completed/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId,
            },
            type: 'post',
            success: function(){
                var cardItem = $('#mail-item[data-id]"') + dataId + '"]';
                cardItem.css('text-decoration', 'line-through').hide().slideDown();
                $('#mail-list').append(cardItem);
            }
        })
    })

})
