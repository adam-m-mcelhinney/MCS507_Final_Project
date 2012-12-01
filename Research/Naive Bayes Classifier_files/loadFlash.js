function loadFlash(movieName, movieWidth, movieHeight, backColour, version, wmode, image, border, ctnt) {
    document.write("<object classid=\"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000\"  width=\"" + movieWidth + "\" height=\"" + movieHeight + "\" id=\"" + ctnt + "\">");
    document.write("<param name=movie value=\"" + movieName + "\">");
    document.write("<param name=menu value=false>");
    document.write("<param name=quality value=high>");
    document.write("<PARAM NAME=bgcolor VALUE=#" + backColour + ">");
    document.write("<param name=wmode value=" + wmode + "> ");
    document.write("<!--[if !IE]>--><object type=\"application/x-shockwave-flash\" data=\"" + movieName + "\" width=\"" + movieWidth + "\" height=\"" + movieHeight + "\"id=\"" + ctnt + "\">");
    document.write("<param name=movie value=\"" + movieName + "\">");
    document.write("<param name=menu value=false>");
    document.write("<param name=quality value=high>");
    document.write("<PARAM NAME=bgcolor VALUE=#" + backColour + ">");
    document.write("<param name=wmode value=" + wmode + "><!--<![endif]--> ");
    document.write("<a href=\"http://statsoft.com/LinkClick.aspx?fileticket=rnwtjqkxtI4%3d&tabid=288&mid=939\" target=\"_blank\"><img src=" + image + " border=" + border + " /></a><!--[if !IE]>--></object><!--<![endif]--></object>");
} 


