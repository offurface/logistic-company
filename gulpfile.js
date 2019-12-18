// Plugins
const task = require('gulp').task
const parallel = require('gulp').parallel
const series = require('gulp').series
const src = require('gulp').src
const spawn = require('child_process').spawn
const open = require('gulp-open')
const fs = require('fs')
const path = require('path')
const wait = require('gulp-wait')

// Config
const config = {
  devServerUrl: 'localhost:8000',
  staticDir: './public/static/',
  distDir: './frontend/static/dist/'
}

function rmDir (dirPath, removeSelf = false) {
  try {
    var files = fs.readdirSync(dirPath)
  } catch (e) { return }
  if (files.length > 0) {
    for (var i = 0; i < files.length; i++) {
      if (files[i] === '.gitignore') { continue }
      var filePath = path.join(dirPath, files[i])
      if (fs.statSync(filePath).isFile()) {
        fs.unlinkSync(filePath)
      } else {
        rmDir(filePath, true)
      }
    }
  }
  if (removeSelf) { fs.rmdirSync(dirPath) }
}

function getNpm () {
  return /^win/.test(process.platform) ? 'npm.cmd' : 'npm'
}

task('runWebpackServer', () => {
  spawn(getNpm(), ['run', 'serve'], {
    stdio: 'inherit'
  })
})

task('runWebpackBuild', done => {
  const proc = spawn(getNpm(), ['run', 'build'], {
    stdio: 'inherit'
  })
  proc.on('exit', () => done())
})

task('runDjangoCollectstatic', done => {
  rmDir(config.staticDir)
  const proc = spawn('pipenv', ['run', 'collectstatic'], {
    stdio: 'inherit'
  })
  proc.on('exit', () => done())
})

task('runDjangoServer', () => {
  spawn('pipenv', ['run', 'server'], {
    stdio: 'inherit'
  })
})

task('openDevServer', () => {
  src(__filename)
    .pipe(wait(6000))
    .pipe(
      open({ uri: `http://${config.devServerUrl}` })
    )
})

task('clear', done => {
  rmDir(config.staticDir)
  rmDir(config.distDir, true)
  done()
})

task('default', parallel(
  'runWebpackServer',
  'runDjangoServer',
  'openDevServer'
))

task('build', series(
  'runWebpackBuild',
  'runDjangoCollectstatic'
))
