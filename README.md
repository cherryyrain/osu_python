# osu_python
An [osu!api](https://github.com/ppy/osu-api) wrapper to be used by Python developers. Please review the osu!api documentation before usage.

# Currently incorrect, trust nothing, the API probably doesn't work

## Installation
The osu_python module can be installed using pip.
On UNIX systems:
```
pip install git+https://github.com/princebee/osu_python.git
```
On Windows:
```
python -m pip install git+https://github.com/princebee/osu_python.git
```

## Usage
The osu_python module allows for all of the functions that the osu!api provides as of Version 1.0. The implementation of these functions varies slightly from accessing the osu!api normally, so please consult the documentation if you have any errors.

### Making an API request
You can submit an API request using `osu_python.make_request(request_type, request_parameters)`.

### Request Types and Parameters
osu_python supports all current request types, as of osu!api version 1.0. The names should be similar, however you do not need to include the `get_` portion of the url. The request parameters *must* be entered as a single dictionary, in the following format: `{"parameter":"value"}`.

**An important thing to note is that the osu!api parameter `type` has been renamed to `utype` in osu_python, due to `type` being a reserved keyword in Python.**

Please consult the osu!api documentation on what each parameter does, as well as whether that parameter is required for the script to run successfully.

| osu_python | osu!api | parameters |
| ---------- | ------- | ---------- |
| `beatmaps` | `/api/get_beatmaps` | `k` `since` `s` `b` `u` `utype` `m` `a` `h` `limit` |
| `user` | `/api/get_user` | `k` `u` `m` `utype` `event_days` |
| `scores` | `/api/get_scores` | `k` `b` `u` `m` `mods` `utype` `limit` |
| `user_best` | `/api/get_user_best` | `k` `u` `m` `limit` `utype` |
| `user_recent` | `/api/get_user_recent` | `k` `u` `m` `limit` `utype` |
| `match` | `/api/get_match` | `k` `mp` |
| `replay` | `/api/get_replay` | `k` `m` `b` `u` |

## Example

### Example Request
```
import osu_python
parameters = {
  "k" : "[valid API key goes here]"
  "u" : "2"
  "m" : "0"
  "utype" : "id"
  "event_days" : "30"
}
print(osu_python.make_request("user",parameters))
```
### Result
```
{"user_id":"2","username":"peppy","count300":"636131","count100":"112461","count50":"23127","playcount":"7072","ranked_score":"412018739","total_score":"1828993065","pp_rank":"243738","level":"65.2278","pp_raw":"757.745","accuracy":"96.67955017089844","count_rank_ss":"16","count_rank_s":"68","count_rank_a":"109","country":"AU","pp_country_rank":"5683","events":[{"display_html":"<b><a href='\/u\/2'>peppy<\/a><\/b> has received the gift of osu! supporter!","beatmap_id":"0","beatmapset_id":"0","date":"2017-07-04 07:26:50","epicfactor":"2"},{"display_html":"<b><a href='\/u\/2'>peppy<\/a><\/b> has received the gift of osu! supporter!","beatmap_id":"0","beatmapset_id":"0","date":"2017-06-18 13:15:43","epicfactor":"2"}]}
```

## Requirements
- Python 3.6.1 (It may work on others, however it has only been tested on 3.6.1)
- [requests](http://docs.python-requests.org/en/master/)
  - Can be installed with `pip install requests` on UNIX systems, or `python -m pip install requests` on Windows.
- A valid osu!api key
  - You can aquire an API key [here](https://osu.ppy.sh/p/api/).
  - **Do *not* share this key with anyone! If you plan on releasing *anything* involving the osu!api, do *not* have your API key in the source, instead prompt the user for their own API key.**
