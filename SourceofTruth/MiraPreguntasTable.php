<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('mira_preguntas', function (Blueprint $table) {
            $table->id();
            $table->tinyInteger('modulo');
            $table->string('tipo', 50)->nullable();
            $table->text('texto');
            $table->text('opciones');
            $table->string('idioma', 100)->nullable();
            $table->timestampsTz();
            $table->userstamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('mira_preguntas');
    }
};



//el objetivo de ese .php es que podamos entneder donde se insertarian las preguntas yasi entender el formato que le debemos dar 