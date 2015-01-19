Container for python development with the Google AppEngine SDK. This container
promises no persistence and you will need to create a storage-only container
and use its volumes if you wish storage to persist between pulls and rebuilds.

Usage:

- Launch a storage-only container and make UID 1000 owner of volume:
    `docker run --name gae-storage-container -v /.appengine_storage debian chown -R 1000:1000 /.appengine_storage`
- Launch your run container using the volumes from the storage container and bind your app as a volume:
    `docker run -ti --volumes-from gae-storage-container -v /path/to/my/app:/app rehabstudio/appengine-dev dev_appserver.py /app`

N.B. You will also want to expose the serving ports using `-p 0.0.0.0:8080:8080` and `8000` for admin
