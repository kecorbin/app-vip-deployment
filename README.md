# app-vip-deployment


# Sample Usage

```
app-vip-deployment TEST_APP1
 dns_name myapp.acme.com

 gtm gtm0

 gtm gtm1
 
 ltm ltm0
  vip_address 1.1.1.1
  vip_port    443
  nodes app1_node1
   address 11.11.11.1
   port    443
  !
  nodes app1_node2
   address 11.11.11.2
   port    443
  !
 !
 ltm ltm1
  vip_address 2.2.2.2
  vip_port    443
  nodes app1_node1
   address 22.22.22.1
   port    443
  !
  nodes app1_node2
   address 22.22.22.2
   port    443
  !

```

# Credits

This is a generated Python package, made by:

  ncs-make-package --service-skeleton python-and-template \
                   --component-class main.Main app-vip-deployment

It contains a dummy YANG model which implements a minimal Service
and an Action that doesn't really do anything useful. They are
there just to get you going.

You will also find two test cases in:

  test/internal/lux/service/
  test/internal/lux/action/

that you can run if you have the 'lux' testing tool.
Your top Makefile also need to implement some Make targets
as described in the Makefiles of the test cases.
You can also just read the corresponding run.lux tests and
do them manually if you wish.

The 'lux' test tool can be obtained from:

  https://github.com/hawk/lux.git
