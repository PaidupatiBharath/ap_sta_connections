
<h1>Hello {{fold}}</h1>


<TABLE  BORDER="n">
   <TR>
      <TH COLSPAN="3">
         <H3><BR>Connected List</H3>
      </TH>
   </TR>

   <TR>
      <TH>S.No</TH>
      <TH>Mac Address</TH>
      <TH>IP Address</TH>
   </TR>

# % for mac_addr, ip_addr in d.items():
#    <TR>
#         <TH>s_no</TH>
# 	<TH>mac_addr</TH>
# 	<TH>ip_addr</TH>
#    </TR>