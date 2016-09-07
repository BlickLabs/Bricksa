/*jshint node: true, indent: 2, nomen:true */
'use strict';

module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      styl: {
        files: ['app/styl/*.styl', 'app/styl/*/*.styl'],
        tasks: ['compileStylus']
      },
      js: {
        files: ['app/js/*.js'],
        tasks: ['compileJavascript']
      },
      etc: {
        files: ['app/favicon.png', 'app/fonts/*.*', 'app/img/*.*', 'app/img/icons/*.*', 'app/img/icons/*/*.*', 'app/img/logos/*.*'],
        tasks: ['copy']
      },
    },
    stylus: {
      options: {
        use : [
          function () {
            return require('autoprefixer-stylus')('last 2 versions', 'ie 8');
          }
        ],
        define: {
          import_tree: require('stylus-import-tree')
        }
      },
      compile: {
        files: {
          'dist/css/main.min.css': 'app/styl/main.styl'
        }
      }
    },
    jshint: {
      all: ['Gruntfile.js', 'app/js/*.js'],
      options: {
        browser: true,
        indent: 2,
        devel: true,
        globals: {
          '$': true,
          'jQuery': true
        }
      }
    },
    concat: {
      options: {
        separator: ''
      },
      basic: {
        src: ['app/js/*.js'],
        dest: 'dist/js/app.js'
      }
    },
    bower_concat: {
      all: {
        dest: {
          js: 'dist/js/bower_dependencies.js',
          css: 'dist/css/bower_dependencies.min.css'
        },
        dependencies: {
          'bootstrap': 'jquery',
          'slick-carousel': 'jquery',
          'jquery-validation': 'jquery'
        },
        mainFiles: {
          'bootstrap': ['dist/js/bootstrap.min.js', 'dist/css/bootstrap.min.css'],
          'slick-carousel' : ['slick/slick.min.js', 'slick/slick.css'],
          'font-awesome': ['css/font-awesome.min.css']
        }
      }
    },
    uglify: {
      app: {
        options: {},
        files: {
          'dist/js/app.min.js': ['<%= concat.basic.dest %>'],
        }
      },
      bower: {
        options: {},
        files: {
          'dist/js/bower_dependencies.min.js': ['<%= bower_concat.all.dest.js %>']
        }
      }
    },
    copy: {
      all : {
        files : [
          {
            expand : true,
            dest   : 'dist/img',
            cwd    : 'app/img',
            src    : [
              '**/*'
            ]
          },
          {
            expand : true,
            dest   : 'dist/fonts',
            cwd    : 'app/fonts',
            src    : [
              '**/*'
            ]
          },
          {
            src: 'app/favicon.png',
            dest: 'dist/favicon.png'
          },
          {
            expand : true,
            dest   : 'dist/fonts',
            cwd    : 'bower_components/font-awesome/fonts',
            src    : [
              '**/*'
            ]
          }
        ]
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.registerTask('default', ['stylus', 'jshint', 'concat', 'bower_concat', 'uglify', 'copy', 'watch']);
  grunt.registerTask('nowatch', ['stylus', 'jshint', 'concat', 'bower_concat', 'uglify', 'copy']);
  grunt.registerTask('compileStylus', ['stylus']);
  grunt.registerTask('compileJavascript', ['jshint', 'concat', 'uglify:app']);
  grunt.registerTask('compileBower', ['bower_concat', 'uglify:bower']);
};
