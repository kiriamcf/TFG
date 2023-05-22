<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\SongScriptRequest;
use App\Http\Requests\AlbumScriptRequest;
use App\Http\Requests\DownloadRequest;
use Illuminate\Support\Facades\Storage;

class ScriptController extends Controller
{
    /**
     * Execute image generator python script.
     *
     * @param  ScriptRequest  $request
     * @return Response
     */
    public function song(SongScriptRequest $request)
    {   
        set_time_limit(0);

        $lyrics = str_replace("\n", ' ', $request->lyrics);

        $resolution = $request->resolution;

        $genre = $request->genre;

        $songName = '"' . $request->songName . '"';

        $artist = '"' . $request->artist . '"';
        
        $words = array_filter(array_map(fn ($word) => trim($word), explode(' ', $lyrics)));      
        
        $lyrics = '"' . implode(' ', $words) . '"';
        
        $path = base_path('\scripts\main.py');
        
        $output = exec("python $path song $artist $songName $genre $lyrics $resolution");

        $url = Storage::disk('public')->url($output);

        return ["url" => $url];
    }

    /**
     * Execute image generator python script.
     *
     * @param  ScriptRequest  $request
     * @return Response
     */
    public function album(AlbumScriptRequest $request)
    {   
        set_time_limit(0);

        $songs = array_map(fn ($song) => str_replace("\n", ' ', $song), $request->songs);

        $resolution = $request->resolution;

        $genre = $request->genre;

        $albumName = '"' . $request->albumName . '"';

        $artist = '"' . $request->artist . '"';

        $songNames = [];

        $albumWords = [];

        foreach ($songs as $song) {
            array_push($songNames, $song["songName"]);
            $songWords = array_filter(array_map(fn ($word) => trim($word), explode(' ', $song["lyrics"])));
            $albumWords = array_merge($albumWords, $songWords);
        }    
        
        $lyrics = '"' . implode(' ', $albumWords) . '"';
        
        $path = base_path('\scripts\main.py');
        
        $output = exec("python $path album $artist $albumName $genre $lyrics $resolution");

        $url = Storage::disk('public')->url($output);

        return ["url" => $url];
    }
}
