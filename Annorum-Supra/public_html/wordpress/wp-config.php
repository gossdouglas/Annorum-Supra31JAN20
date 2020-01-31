<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'goss_cmps394_wordpress' );

/** MySQL database username */
define( 'DB_USER', 'goss' );

/** MySQL database password */
define( 'DB_PASSWORD', 'w0148941' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'vjmDH1{T_OB6q+DJCOL^=,gv(qZ59I;P<^$W2OZl&iA9ih4Ch_2Plr TGKc@e>EK' );
define( 'SECURE_AUTH_KEY',  '<hVM9o:nRd!~eIMpKlT[>.GA7nN=8ylJSk8];LDsB+yaM<hPNS0?G!Qv0F.vWrTa' );
define( 'LOGGED_IN_KEY',    '_FG4]oPAY]%mX!r*Ej]m*K/TGv!<v_sAKz#Z#.cIsN-E85,xoT|Rs[*->|GXQ5l(' );
define( 'NONCE_KEY',        '6wj/:q/$-,)]&D)xy?40Tc@u<`!WzC,7&OV;ZD4;[)n3;2Q.xo*t%Jxo9Ff;0Y6_' );
define( 'AUTH_SALT',        '4*T`> ~wkB,58TS[%HO,Wf-p(;NT]%I6h/(l&!JZ^hFhUUL8~SL r/X=>{#s`=4<' );
define( 'SECURE_AUTH_SALT', '>Vjad/ v,QY^/m|gjyDf2qqj6#Vf?6N2>?=?C>r?BLWHaO~E-JJ)pOGQ[YB(On{ ' );
define( 'LOGGED_IN_SALT',   'He9dkSQU;yYg5 ?aQD/o3?!2*0BMpa#^{&Wxpf#J<PT/>D{hw8n;S/pEl+zh=3U6' );
define( 'NONCE_SALT',       'Mg/2c[rQpYlHEL09!x-R$0;i8z0@J@=A4l9*AS~`ZT&VbzK&l(NppTVh5`Oo-O,V' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );