<?php

namespace App\Http\Requests;
use Illuminate\Validation\Rule;


use Illuminate\Foundation\Http\FormRequest;

class SongScriptRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array|string>
     */
    public function rules(): array
    {
        return [
            'lyrics' => 'required|string',
            'genre' => 'required|string',
            'artist' => 'required|string',
            'songName' => 'required|string',
            'resolution' => [
                'required',
                'integer',
                Rule::in([512, 728])
            ],
        ];
    }
}
