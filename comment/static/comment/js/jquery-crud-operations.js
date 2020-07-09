/*
This file contain redundant code when performing the crud operation 
i like it to be this way (to make the code plugable -until another situation is encountered-)
*/
// wait until all html tags are rendered
$(function () {

    // when the user click on 'New Comment'
    $(".js-create-comment").click(function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                // open the Bootstrap Modal before the Ajax request starts
                $("#modal-comment").modal("show");
            },
            success: function (data) {
                // set the partial_comment_create.html in our template
                $("#modal-comment .modal-content").html(data.html_form);
            }
        });
    });

    // when the user submit the comment form
    $("#modal-comment").on("submit", ".js-comment-create-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#comment-table tbody").html(data.html_comment_list);  // <-- Replace the table body
                    $("#modal-comment").modal("hide");  // <-- Close the modal
                }
                else {
                    $("#modal-comment .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    /////////////////// Update ///////////////////////
    //
    // when the user click on 'Edit'
    $(".js-update-comment").click(function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                // open the Bootstrap Modal before the Ajax request starts
                $("#modal-comment").modal("show");
            },
            success: function (data) {
                // set the partial_comment_create.html in our template
                $("#modal-comment .modal-content").html(data.html_form);
            }
        });
    });


    // when the user submit the comment form
    $("#modal-comment").on("submit", ".js-comment-update-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#comment-table tbody").html(data.html_comment_list);  // <-- Replace the table body
                    $("#modal-comment").modal("hide");  // <-- Close the modal
                }
                else {
                    $("#modal-comment .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


    /////////////////// Delete ///////////////////////
    //
    // when the user click on 'Delete'
    $(".js-delete-comment").click(function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                // open the Bootstrap Modal before the Ajax request starts
                $("#modal-comment").modal("show");
            },
            success: function (data) {
                // set the partial_comment_create.html in our template
                $("#modal-comment .modal-content").html(data.html_form);
            }
        });
    });


    // when the user submit the comment form
    $("#modal-comment").on("submit", ".js-comment-delete-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                $("#comment-table tbody").html(data.html_comment_list);  // <-- Replace the table body
                $("#modal-comment").modal("hide");  // <-- Close the modal
            }
        });
        return false;
    });


});
