#MinecraftSkin-Python
我自己的一个小程序，旨在模拟skins.minecraft.net  
这是python版，如果您重构了其他的语言版本，请联系我，我qq250445577，谢谢  
该项目由django制作
##调用格式
###get
直接访问ip:端口/用户名.png，例如
>127.0.0.1:8000/pppwaw.png

会通过302跳转至材质网站，例如
>http://textures.minecraft.net/texture/68a58b451270c1f57ba0e56c001feed199dcb49c32dc170b533a813d45bbd299  
![我的皮肤](http://textures.minecraft.net/texture/68a58b451270c1f57ba0e56c001feed199dcb49c32dc170b533a813d45bbd299)
###post
post要post到ip:端口/api上，例如
>127.0.0.1:8000/api

总共有三个参数，分别是

名字|解释|例子
:-:|:-:|:-:
get|这个参数决定了要调用的功能|get=all
uuid|和name二选一，这个参数决定了要调用的功能|uuid=a216b4dc4a6344e193169ca39bfb8356
name|和uuid二选一这个参数决定了要调用的功能|name=pppwaw
=======
MinecraftSkin-Python
我自己的一个小程序，旨在复原skins.minecraft.net
这是python版，如果您重构了其他的语言版本，请联系我，我qq250445577，谢谢
>>>>>>> e34160a800e8e95c280b66879bf36f3fdee4ed5b
