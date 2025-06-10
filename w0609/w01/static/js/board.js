function writeBtn(){
    if('{{request.session.session_id}}'){
        alert("로그인을 하셔야 게시글 작성이 가능합니다.");
        location.href='/member/login/';
        return;
    }else{
        alert("로그인이 되었습니다. 게시글 작성이 가능합니다.")
    }

    if($(".btitle").val().length<2){
        alert("제목은 한글자 이상 입력하셔야 합니다.");
        $(".btitle").focus();
        return;
    }
    alert('게시글을 등록합니다.')
    // writeFrm.submit();
}