# Mythical

Yet another Kodi plugin for MythTV.

## Why?

I needed a simple MythTv plugin for Kodi, so here is the one I wrote.

I am sharing this in hopes that someone else may find it useful.

## Kodi 18 and before

They switched to [Python3 in Kodi 19](https://kodi.wiki/view/General_information_about_migration_to_Python_3) and after.

The addon zip that works for Python 2.x is at https://github.com/evuraan/Mythical/tree/MythTV_Plugin_For_Pre_Python3_Kodi - download the plugin zip and follow instructions from there.

If you are using Kodi 19 and after, read on.

## Setting up

Since you have a MythBackend running, it is assumed that you've the technical prowess to plough through the three simple steps involved.

#### Step 1 : Setup your BaseURL

In most cases, MythTV records to `/var/lib/mythtv/recordings` folder. We need to make this folder available for Kodi to do HTTP GETs.

If you have apache, the following would allow internal network 192.168.1.0/24 to access this directory. That is, if your MythTV backend server is at IP 192.168.1.100, you'd now be able to reach`http://192.168.1.100/recordings/`from your local network.

```html
 Alias /recordings/ "/var/lib/mythtv/recordings/"
    <Directory "/var/lib/mythtv/recordings/">
    AllowOverride None
    Require ip 192.168.1.0/24
 </Directory>
```

(Natrually you will need to replace the IP with one that matches your internal network.)

#### Step 2 : Setup generate_info cronjob

Next, we need to setup a cron job that would generate `/var/lib/mythtv/recordings/recordings.txt` - I've two scripts with the same functionality : a python script [generate_info.py](https://github.com/evuraan/Mythical/blob/master/scripts/generate_info.py), or a bash variant, [generate_info.sh](https://github.com/evuraan/Mythical/blob/master/scripts/generate_info.sh) - pick whichever you're comfortable with.

Setting up generate_info.sh:

```bash
$ wget https://raw.githubusercontent.com/evuraan/Mythical/master/scripts/generate_info.sh -O /usr/local/bin/generate_info.sh
$ chmod u+x  /usr/local/bin/generate_info.sh
$ echo "*/15 * * * *   `whoami` /usr/local/bin/generate_info.sh 1>/dev/null 2>/dev/null || :" | sudo tee -a /etc/crontab
```

Or, setting up generate_info.py:

```bash
$ wget https://raw.githubusercontent.com/evuraan/Mythical/master/scripts/generate_info.py -O /usr/local/bin/generate_info.py
$ chmod u+x  /usr/local/bin/generate_info.py
$ echo "*/15 * * * *   `whoami` /usr/local/bin/generate_info.py 1>/dev/null 2>/dev/null || :" | sudo tee -a /etc/crontab
```

Please verify that you see `/var/lib/mythtv/recordings/recordings.txt` updated every 15 minutes, as this is an important step.

#### Step 3 : Install Kodi plugin Mythical

Download and install the `plugin.video.Mythical.zip` from "[Releases](https://github.com/evuraan/Mythical/releases)" tab.

By default, the plugin uses a pre-defined set of free sample videos from my server - we need to change this so it uses _yours_ instead. Modify your `$HOME/.kodi/addons/plugin.video.Mythical/main.py` with your BaseUrl from Step 1 above:

```Python
BaseURL = "http://192.168.1.100/recordings/"
```

#### Notes

- Heavily influenced by [romanvm's](https://github.com/romanvm/plugin.video.example) example plugin.
- If your recordings are MPEG files, I suggest you setup [video cache](https://kodi.wiki/view/HOW-TO:Modify_the_video_cache) for Kodi. Here is my `advancedsettings.xml`:

```xml
<advancedsettings>
<cache>
    <memorysize>0</memorysize>
   <buffermode>2</buffermode>
   <readfactor>80</readfactor>
</cache>
</advancedsettings>
```

- Please consider Giving to your [PBS Station.](https://www.pbs.org/foundation/ways-to-give/)

License: [GPL v.3](http://www.gnu.org/copyleft/gpl.html)
