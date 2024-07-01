// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

const { defineConfig } = require('@vue/cli-service')
const envallowedHosts = process.env.BK_ALLOWED_HOST.split(',');
module.exports = defineConfig({
    configureWebpack: {
      entry: "./src/main.js",
      watch: true,
      watchOptions: {
        ignored: /node_modules/,
        poll: 1000,
      },
    },
    devServer: {
      hot: true,
      allowedHosts: envallowedHosts,
    },
    transpileDependencies: true,
  });

// module.exports = defineConfig({
//   configureWebpack: {
//       entry: "./src/main.js",
//       devServer: {
//           hot: true,
//       },
//       watch: true,
//       watchOptions: {
//           ignored: /node_modules/,
//           poll: 1000,
//       },
//   },
//   transpileDependencies: true,
// });

