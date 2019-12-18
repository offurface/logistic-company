const path = require('path')
const isProd = process.env.NODE_ENV === 'production'
const BundleTracker = require('webpack-bundle-tracker')

// Config
function Config () {
  const frontendDir = path.join(__dirname, 'frontend')
  const staticDir = path.join(frontendDir, 'static')
  const appsDir = path.join(__dirname, 'backend', 'apps')
  const templatesDir = path.join(frontendDir, 'templates')
  return {
    appsDir: appsDir,
    staticDir: staticDir,
    frontendDir: frontendDir,
    templatesDir: templatesDir,
    jsDir: path.join(frontendDir, 'js'),
    distDir: path.join(staticDir, 'dist'),
    sassDir: path.join(frontendDir, 'sass'),
    webpackStatsDir: path.join('frontend', 'static', 'dist'),
    globalStyle: [ 'style/abstracts' ]
  }
}

const globalConfig = Config()

function loadGlobalStyles () {
  return globalConfig.globalStyle
    .map(path => `@import "${path}"`)
    .join('\n')
}

module.exports = {
  publicPath: isProd ? 'static/dist' : 'http://localhost:8080/dist',
  outputDir: globalConfig.distDir,
  css: {
    loaderOptions: {
      sass: {
        data: loadGlobalStyles()
      }
    }
  },
  chainWebpack: config => {
    config
      .entry('app')
      .clear()
      .add('./frontend/js/app.js')
      .end()
    config.plugins.delete('html')
    config.plugins.delete('preload')
    config.plugins.delete('prefetch')
    config.plugins.delete('copy')
    config.resolve.alias
      .set('@', globalConfig.jsDir)
      .set('style', globalConfig.sassDir)
      .set('vue$', 'vue/dist/vue.esm.js')
    config.devServer
      .public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .contentBase(globalConfig.templatesDir)
      .watchContentBase(true)
      .headers({ 'Access-Control-Allow-Origin': ['*'] })
  },
  configureWebpack: config => {
    config.plugins.push(new BundleTracker({
      path: globalConfig.webpackStatsDir,
      filename: 'webpack-stats.json'
    }))
  }
}
