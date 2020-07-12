$(function () {

    $("#login-form").on("submit", function () {
        var formObj = $(this);

        try {
            var formData = formObj.serializeArray();
            $.ajax({
                type: "POST",
                url: formObj.attr("action"),
                data: formData,
                dataType: "json",
                success: function (data) {
                    formObj.find(".messages").html("");
                    if (data.status === "error") {
                        formObj.find(".messages").html(data.error_message);
                        return;
                    }

                    $(":submit").attr("disabled", true);
                    setTimeout(function () {
                        window.location.href = webconfig["base_url"] + "home"
                    }, 1000);

                }
            })
        } catch (e) {
            console.log(e);
        }

        return false;
    });


    $("#signup-form").on("submit", function () {
        var formObj = $(this);

        try {
            var formData = formObj.serializeArray();
            $.ajax({
                type: "POST",
                url: formObj.attr("action"),
                data: formData,
                dataType: "json",
                success: function (data) {
                    formObj.find(".messages").html("");
                    if (data.status === "error") {
                        formObj.find(".messages").html(data.error_message);
                        return;
                    }

                    $(":submit").attr("disabled", true);

                    $("#signup-modal").modal()
                    $("#signup-modal").modal("show")

                    /*setTimeout(function () {
                        window.location.href = webconfig["base_url"] + "/auth/login"
                    }, 1000);*/

                }
            })
        } catch (e) {
            console.log(e);
        }

        return false;
    });



    $("#tweet-form").on("submit", function () {
        var formObj = $(this);

        try {
            var formData = formObj.serializeArray();
            $.ajax({
                type: "POST",
                url: formObj.attr("action"),
                data: formData,
                dataType: "json",
                success: function (data) {
                    formObj.find(".messages").html("");
                    if (data.status === "error") {
                        formObj.find(".messages").html(data.error_message);
                        return;
                    }

                    /*setTimeout(function () {
                        window.location.href = webconfig["base_url"] + "/auth/login"
                    }, 1000);*/

                }
            })
        } catch (e) {
            console.log(e);
        }

        return false;
    });

});