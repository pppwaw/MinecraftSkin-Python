from MinecraftSkin import mc
from django import http
def get(request,name):
    name=name.split(".")
    uuid=mc.get_uuid(name[0])
    if uuid == None:
        return http.Http404()
    else:
        return http.HttpResponseRedirect(mc.get_skin(uuid))
def post(request):
    print (request.POST["get"])
    if "uuid" in request.POST.keys():
        uuid = request.POST["uuid"]
    elif "name" in request.POST.keys():
        name = request.POST["name"]

    else:
        return http.Http404()
    if "get" not in request.POST.keys():
        return http.Http404()
    if request.POST["get"] == "skin":
        try:
            skinurl = mc.get_skin(uuid)
        except:
            uuid = mc.get_uuid(name)
            skinurl = mc.get_skin(uuid)
        finally:
            return http.HttpResponseRedirect(skinurl)
    elif request.POST["get"] == "cape":
        try:
            capeurl = mc.get_cape(uuid)
        except:
            uuid = mc.get_uuid(name)
            capeurl = mc.get_cape(uuid)
        finally:
            if capeurl == None:
                return http.Http404()
            return http.HttpResponseRedirect(capeurl)
    elif request.POST["get"] == "all":
        try:
            alljson = mc.get_skin_and_cape(uuid)
        except:
            uuid = mc.get_uuid(name)
            alljson = mc.get_skin_and_cape(uuid)
        finally:
            return http.JsonResponse(alljson)
    return http.HttpResponse()